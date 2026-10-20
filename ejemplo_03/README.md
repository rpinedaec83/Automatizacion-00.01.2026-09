# EJEMPLO 03: Laboratorio de Agentes - OpenAI & DeepSeek en Vivo
## Subindicador 3: Fundamentos de Agentes de IA, Streaming y Casos Prácticos

Esta aplicación interactiva cuenta con dos implementaciones completas e independientes (**Node.js** y **Python**) que se comunican mediante WebSockets (Socket.IO) con streaming token a token a los modelos de **OpenAI** (`gpt-4o-mini`, `gpt-4o`) y **DeepSeek** (`deepseek-chat`, `deepseek-reasoner`).

---

### 📋 Requisitos Previos

1. **API Keys**:
   - OpenAI API Key (`sk-...`)
   - DeepSeek API Key (`sk-...`) *(opcional si solo pruebas OpenAI)*
2. **Entorno de ejecución**:
   - **Node.js** (v18+) para la versión Node.
   - **Python** (3.10+) para la versión Python.

---

### ⚙️ Configuración de Variables de Entorno (`.env`)

Antes de iniciar cualquiera de las dos versiones, configura tus claves API:

#### En Node.js (`ejemplo_03/node/`):
Copia el archivo de ejemplo y edítalo con tus claves:
```bash
cd ejemplo_03/node
cp .env.sample .env
```
Contenido de `.env`:
```env
OPENAI_API_KEY=tu_api_key_de_openai
DEEPSEEK_API_KEY=tu_api_key_de_deepseek
PORT=3000
```

#### En Python (`ejemplo_03/python/`):
Copia el archivo de ejemplo y edítalo con tus claves:
```bash
cd ejemplo_03/python
cp .env.example .env
```
Contenido de `.env`:
```env
OPENAI_API_KEY=tu_api_key_de_openai
DEEPSEEK_API_KEY=tu_api_key_de_deepseek
PORT=5001
```

---

### 🚀 Cómo Iniciar la Aplicación

Puedes ejecutar la versión que prefieras (ambas tienen la misma interfaz y funcionalidad).

#### Opción A: En Node.js (Puerto 3000)

```bash
cd ejemplo_03/node
npm install
npm start
```
*(O simplemente ejecuta el script de inicio directo: `./run.sh`)*

👉 Abrir en el navegador: **`http://localhost:3000`**

---

#### Opción B: En Python (Puerto 5001)

```bash
cd ejemplo_03/python
python3 -m venv .venv
source .venv/bin/activate       # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
*(O simplemente ejecuta el script de inicio directo: `./run.sh`)*

👉 Abrir en el navegador: **`http://localhost:5001`**

---

### 🧪 Casos Prácticos Incluidos en el Laboratorio

La interfaz incluye 4 casos de negocio precargados con System Prompts y botones para cargar preguntas de prueba:

#### 1. Caso 1: Soporte al Cliente (Tier 1) - Reglas y Derivación Humana
* **Objetivo:** Mostrar cómo el agente aplica políticas estrictas de cambios/devoluciones y activa la bandera especial `[DERIVAR_A_HUMANO]` cuando el cliente está insatisfecho o amenaza con quejas legales.
* **Resaltado en Interfaz:** Si el agente emite la derivación, la respuesta se resalta con alerta roja de escalamiento.

#### 2. Caso 2: Generador de Contenido Multicanal (B2B)
* **Objetivo:** Tomar un lanzamiento técnico o actualización y adaptarlo simultáneamente a dos formatos:
  1. *LinkedIn:* Reflexivo, profesional, con gancho y hashtags.
  2. *WhatsApp Business:* Dinámico, conciso, con viñetas y emojis.

#### 3. Caso 3: Extracción y Clasificación a JSON Estricto
* **Objetivo:** Demostrar cómo estructurar la salida de un ticket de operaciones en un JSON validable (`categoria`, `monto_involucrado`, `urgencia`, `sentimiento`), empleando temperatura `0.0` y modo objeto JSON.

#### 4. Caso 4: Minuta Ejecutiva y Tareas de Productividad
* **Objetivo:** Tomar notas caóticas de una reunión y organizarlas en objetivos, acuerdos clave y una tabla de acciones con responsables y fechas límite.

---

### 🎛️ Controles en la Interfaz

* **Proveedor de IA:** Alterna con 1 clic entre **OpenAI** y **DeepSeek**.
* **Selector de Modelos:** `gpt-4o-mini`, `gpt-4o`, `deepseek-chat` (V3) y `deepseek-reasoner` (R1 con razonamiento).
* **Parámetros en Vivo:** Ajusta Temperatura (`0.0` a `1.0`), Max Tokens y Formato de Salida (`Markdown` vs `JSON`).
* **Cargar Prompt de Prueba:** Botón para rellenar automáticamente la consulta típica de cada caso.
