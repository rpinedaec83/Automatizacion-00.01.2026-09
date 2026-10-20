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

// Helper para crear clientes dinámicamente según el proveedor
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

// Historial en memoria por cliente
const conversations = new Map();

io.on('connection', (socket) => {
  console.log(`Cliente conectado: ${socket.id}`);

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
        maxTokens = 400,
        isJson = false,
      } = data;

      let history = conversations.get(socket.id);

      // Si no existe historial o cambió el system prompt
      if (!history || history.length === 0 || history[0].content !== systemPrompt) {
        history = [{ role: 'system', content: systemPrompt }];
      }

      history.push({ role: 'user', content: text });
      conversations.set(socket.id, history);

      // Instanciar cliente (OpenAI o DeepSeek)
      const client = getClient(provider);

      // Parámetros de llamada universales (Chat Completions Streaming)
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

      // Guardar en historial
      history.push({ role: 'assistant', content: fullBotReply });

      const escalado =
        fullBotReply.includes('[DERIVAR_A_HUMANO]') ||
        fullBotReply.includes('[TRANSFERIR_AGENTE_HUMANO]');

      socket.emit('stream_end', { fullText: fullBotReply, escalado, isJson });

    } catch (error) {
      console.error('Error con LLM:', error);
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
    console.log(`Cliente desconectado: ${socket.id}`);
  });
});

const PORT = process.env.PORT || 3000;
httpServer.listen(PORT, () => {
  console.log(`Servidor Node.js (OpenAI + DeepSeek) corriendo en http://localhost:${PORT}`);
});
