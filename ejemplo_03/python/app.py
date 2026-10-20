import os
import socketio
import uvicorn
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(
    sio, 
    static_files={
        '/': './public/index.html',
        '/static': './public'
    }
)

def get_client(provider: str):
    if provider == "deepseek":
        return OpenAI(
            api_key=os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY"),
            base_url="https://api.deepseek.com"
        )
    return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

conversations = {}

@sio.event
async def connect(sid, environ):
    print(f"Cliente conectado: {sid}")
    conversations[sid] = []

@sio.event
async def set_case(sid, data):
    system_prompt = data.get("systemPrompt", "")
    conversations[sid] = [{"role": "system", "content": system_prompt}]
    await sio.emit("case_updated", {"status": "ok"}, to=sid)

@sio.event
async def user_message(sid, data):
    user_text = data.get("text", "")
    system_prompt = data.get("systemPrompt", "")
    provider = data.get("provider", "openai")
    model = data.get("model", "gpt-4o-mini")
    temperature = float(data.get("temperature", 0.2))
    max_tokens = int(data.get("maxTokens", 400))
    is_json = bool(data.get("isJson", False))

    history = conversations.get(sid, [])
    if not history or history[0]["content"] != system_prompt:
        history = [{"role": "system", "content": system_prompt}]

    history.append({"role": "user", "content": user_text})
    conversations[sid] = history

    client = get_client(provider)
    full_reply = ""

    try:
        call_params = {
            "model": model,
            "messages": history,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True,
        }

        if is_json:
            call_params["response_format"] = {"type": "json_object"}

        stream = client.chat.completions.create(**call_params)

        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            if delta:
                full_reply += delta
                await sio.emit("stream_chunk", {"delta": delta}, to=sid)

        history.append({"role": "assistant", "content": full_reply})

        escalado = "[DERIVAR_A_HUMANO]" in full_reply or "[TRANSFERIR_AGENTE_HUMANO]" in full_reply
        await sio.emit("stream_end", {"fullText": full_reply, "escalado": escalado, "isJson": is_json}, to=sid)

    except Exception as e:
        print(f"Error procesando {provider}: {e}")
        await sio.emit("stream_error", {"error": str(e)}, to=sid)

@sio.event
async def clear_history(sid, data):
    system_prompt = data.get("systemPrompt", "")
    conversations[sid] = [{"role": "system", "content": system_prompt}]
    await sio.emit("history_cleared", to=sid)

@sio.event
async def disconnect(sid):
    conversations.pop(sid, None)
    print(f"Cliente desconectado: {sid}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"Servidor Python (OpenAI + DeepSeek) corriendo en http://localhost:{port}")
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
