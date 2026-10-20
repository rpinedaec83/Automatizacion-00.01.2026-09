# EJEMPLO 04: Laboratorio Interactivo de Prompts para Agentes
## Subindicador 4: Diseño de Prompts Efectivos, R-C-T-R-F, Delimitadores y Few-Shot

Esta aplicación interactiva cuenta con dos implementaciones completas e independientes (**Python** y **Node.js**) que se conectan mediante WebSockets (Socket.IO) con streaming token a token a los modelos de **OpenAI** (`gpt-4o-mini`, `gpt-4o`) y **DeepSeek** (`deepseek-chat`, `deepseek-reasoner`).

---

### 🚀 Cómo Iniciar la Aplicación

#### Opción A: En Node.js (Puerto 3001)
```bash
cd ejemplo_04/node
./run.sh
```
*(o alternativamente: `npm start`)*  
👉 Abrir en el navegador: **`http://localhost:3001`**

---

#### Opción B: En Python (Puerto 5002)
```bash
cd ejemplo_04/python
./run.sh
```
*(o alternativamente: `python app.py`)*  
👉 Abrir en el navegador: **`http://localhost:5002`**

---

### 🧪 Casos Didácticos Interactivos Incluidos

#### 1. Caso 1: Deconstrucción A/B (Prompt Vago vs. Fórmula R-C-T-R-F)
* **Objetivo:** Demostrar cómo un prompt sin estructura genera salidas desordenadas e inútiles para un CRM, mientras que la fórmula **R-C-T-R-F** genera una tabla de calificación de leads B2B impecable.
* **Control Interactivo:** Botón switch para alternar en vivo entre `Modo Vago ❌` y `Modo R-C-T-R-F ✅`.
* **Pruebas Rápidas:** Lead caliente (35 colaboradores), Lead tibio (sin datos) y No califica (2 colaboradores).

#### 2. Caso 2: Base Delimitada & Grounding (`<reglamento_laboral>`)
* **Objetivo:** Mostrar cómo las etiquetas semánticas aíslan el manual de RRHH y la regla de "caso negativo" evita que el agente alucine bonos o beneficios inexistentes.
* **Pruebas Rápidas:** Consulta válida de descanso médico, Pregunta trampa sobre bono escolar de marzo, e Intento de inyección (Jailbreak).

#### 3. Caso 3: Few-Shot Prompting (Normalización de Catálogo)
* **Objetivo:** Comparar cómo responde el agente en `Modo Zero-Shot ⚡` (texto explicativo libre) frente a `Modo Few-Shot 🎯` (formato canónico rígido de inventario en una sola línea).
* **Control Interactivo:** Botón switch para activar/desactivar los ejemplos Few-Shot en vivo.
* **Pruebas Rápidas:** Títulos sucios de audífonos Sony, monitor Samsung y teclado Logitech.

#### 4. Caso 4: Auditor QA de Soporte (Rúbrica Cuantitativa sobre 100 Puntos)
* **Objetivo:** Convertir una evaluación cualitativa en una tabla de auditoría con notas matemáticas exactas y dictamen automático (`[APROBADO]` o `[OBSERVADO]`).
* **Pruebas Rápidas:** Transcripción excelente con validación de seguridad (DNI) vs. Transcripción deficiente donde el asesor omite validar identidad.

---

### ⚙️ Características Técnicas
* **Streaming en Tiempo Real:** Visualización fluida token a token sin bloqueos de interfaz.
* **Multi-Proveedor:** Conmutador instantáneo entre **OpenAI** y **DeepSeek**.
* **Badges Semánticos:** Resaltado automático en verde/rojo/ámbar según las decisiones del agente.
* **Control de Parámetros:** Ajuste de Temperature (0.0 a 1.0), Max Tokens y formato de respuesta (Markdown vs JSON).
