import express from 'express';
import { createServer } from 'http';
import { Server } from 'socket.io';
import OpenAI from 'openai';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

dotenv.config();

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer);

function getClient(provider) {
  if (provider === 'deepseek') {
    return new OpenAI({
      apiKey: process.env.DEEPSEEK_API_KEY || process.env.OPENAI_API_KEY,
      baseURL: 'https://api.deepseek.com',
    });
  }
  return new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  });
}

app.use(express.static(path.join(__dirname, 'public')));

const conversations = new Map();

io.on('connection', (socket) => {
  console.log(`Cliente conectado (Node Subindicador 4): ${socket.id}`);

  socket.on('set_case', (data) => {
    const { systemPrompt } = data;
    conversations.set(socket.id, [
      { role: 'system', content: systemPrompt },
    ]);
    socket.emit('case_updated', { status: 'ok' });
  });

  socket.on('user_message', async (data) => {
    try {
      const {
        text,
        systemPrompt,
        provider = 'openai',
        model = 'gpt-4o-mini',
        temperature = 0.2,
        maxTokens = 450,
        isJson = false,
      } = data;

      let history = conversations.get(socket.id);

      if (!history || history.length === 0 || history[0].content !== systemPrompt) {
        history = [{ role: 'system', content: systemPrompt }];
      }

      history.push({ role: 'user', content: text });
      conversations.set(socket.id, history);

      const client = getClient(provider);

      const streamParams = {
        model: model,
        temperature: parseFloat(temperature),
        max_tokens: parseInt(maxTokens, 10),
        messages: history,
        stream: true,
      };

      if (isJson) {
        streamParams.response_format = { type: 'json_object' };
      }

      const stream = await client.chat.completions.create(streamParams);
      let fullBotReply = '';

      for await (const chunk of stream) {
        const delta = chunk.choices[0]?.delta?.content || '';
        if (delta) {
          fullBotReply += delta;
          socket.emit('stream_chunk', { delta });
        }
      }

      history.push({ role: 'assistant', content: fullBotReply });

      const upperReply = fullBotReply.toUpperCase();
      const isAprobado = upperReply.includes('APROBADO');
      const isObservado = upperReply.includes('OBSERVADO');
      const isNoCalifica = upperReply.includes('NO_CALIFICA');
      const isCaliente = upperReply.includes('LEAD_CALIENTE') || upperReply.includes('PRIORITARIO');
      const isNoEstipulado = upperReply.includes('NO SE ENCUENTRA ESTIPULADO') || upperReply.includes('NO CUENTO CON ESA INFORMACIÓN');

      socket.emit('stream_end', {
        fullText: fullBotReply,
        isJson,
        isAprobado,
        isObservado: isObservado || isNoCalifica,
        isCaliente,
        isNoEstipulado,
      });

    } catch (error) {
      console.error('Error procesando LLM en Node:', error);
      socket.emit('stream_error', { error: error.message });
    }
  });

  socket.on('clear_history', (data) => {
    const systemPrompt = data?.systemPrompt || '';
    conversations.set(socket.id, [{ role: 'system', content: systemPrompt }]);
    socket.emit('history_cleared');
  });

  socket.on('disconnect', () => {
    conversations.delete(socket.id);
    console.log(`Cliente desconectado (Node): ${socket.id}`);
  });
});

const PORT = process.env.PORT || 3001;
httpServer.listen(PORT, () => {
  console.log(`Servidor Node.js Subindicador 4 corriendo en http://localhost:${PORT}`);
});
