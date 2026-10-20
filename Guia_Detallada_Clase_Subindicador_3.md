# GUÍA DIDÁCTICA DE CLASE: SUBINDICADOR 3
## Curso: Automatización de Agentes de IA (Pachaqtec / IDAT)

---

### FICHA TÉCNICA
* **Módulo / Unidad:** IL 1 - Fundamentos y Componentes de los Agentes de IA
* **Subindicador Evaluado:** **3. Aplica el análisis de casos reales de agentes de IA para la identificación de oportunidades de automatización en su entorno profesional.**
* **Horario:** Martes y Jueves, 19:30 a 21:45 hrs (Duración: 135 minutos / 2h 15 min)
* **Entorno de Práctica:** OpenAI Platform API (Playground: `platform.openai.com/playground`)
* **Modelo Recomendado:** `gpt-4o-mini` (óptimo en costo y velocidad) y `gpt-4o`

---

## 1. CRONOGRAMA MINUTO A MINUTO (19:30 - 21:45)

| Horario | Duración | Bloque | Actividad Pedagógica y Metodología |
| :--- | :---: | :--- | :--- |
| **19:30 - 19:42** | 12 min | **Apertura & Conexión** | • Bienvenida y asistencia.<br>• Recapitulación exprés de los subindicadores 1 y 2 (Reactivo/Deliberativo/Autónomo; Input $\rightarrow$ LLM $\rightarrow$ Output).<br>• Planteamiento del reto de hoy. |
| **19:42 - 20:10** | 28 min | **Marco Teórico (4 Ejes)** | • Casos de negocio reales: Atención al cliente, Generación de contenido, Automatización de procesos (JSON) y Productividad interna. |
| **20:10 - 20:25** | 15 min | **OpenAI Platform & Playground** | • Diferencias entre ChatGPT y OpenAI Platform.<br>• Roles: System Prompt vs User Prompt.<br>• Parámetros clave: Temperature (0.0 a 1.0), Tokens y Modelos. |
| **20:25 - 20:30** | 5 min | **Pausa Activa / Acceso Técnico** | • Verificación de acceso a la plataforma para todos los alumnos. |
| **20:30 - 21:20** | 50 min | **Laboratorio Hands-On (4 Prácticas)** | • Práctica 1: Soporte con Guardrails y derivación a humano.<br>• Práctica 2: Generación multicanal (LinkedIn vs WhatsApp).<br>• Práctica 3: Extracción a JSON estricto (motor para Make/n8n).<br>• Práctica 4: Minuta ejecutiva y matriz de compromisos. |
| **21:20 - 21:35** | 15 min | **Reto Autónomo en Clase** | • Los alumnos crean un agente para su trabajo y 2 voluntarios comparten pantalla para feedback en vivo. |
| **21:35 - 21:45** | 10 min | **Conclusiones y Próxima Clase** | • Síntesis final de aprendizajes.<br>• Conexión con el Subindicador 4 (Diseño de Prompts avanzados). |

---

## 2. FUNDAMENTOS CONCEPTUALES

### A. Conexión Pedagógica (Subíndices 1 y 2 $\rightarrow$ Subíndice 3)
1. **Subindicador 1:** Se definieron los tipos de agentes:
   * *Reactivo:* Actúa ante estímulos inmediatos sin memoria ni planificación.
   * *Deliberativo:* Posee un modelo del entorno, evalúa reglas y planifica antes de ejecutar.
   * *Autónomo:* Capaz de tomar decisiones orientadas a metas y usar herramientas externas sin supervisión constante.
2. **Subindicador 2:** Se identificó la arquitectura básica:
   $$\text{Input (Entrada)} \longrightarrow \text{LLM + Lógica (System Prompt)} \longrightarrow \text{Output (Acción / Texto / JSON)}$$
3. **Subindicador 3 (Hoy):** ¿Cómo convertimos esta arquitectura en soluciones reales de negocio con retorno de inversión?

### B. Los 4 Casos de Uso Empresariales
1. **Atención al Cliente (Customer Support Tier 1):**
   * Resuelve hasta el 80% de preguntas frecuentes.
   * Aplica *Guardrails* (políticas estrictas de devolución y garantías).
   * Activa *Escalamiento Humano* cuando hay enojo, riesgo legal o casos fuera de política.
2. **Generación de Contenido Multicanal:**
   * Mantiene el *Brand Voice* (tono de voz de marca).
   * Adapta un único hecho en publicaciones para LinkedIn, WhatsApp Business o correo masivo.
3. **Automatización de Procesos (RPA Cognitivo & JSON):**
   * Convierte texto desordenado en lenguaje humano a un objeto estructurado `JSON`.
   * Es el puente fundamental para conectar la IA con plataformas No-Code como Make, Zapier y n8n.
4. **Productividad Personal y de Equipos:**
   * Convierte transcripciones o notas sueltas en minutas estructuradas con responsables y fechas límite.

---

## 3. LABORATORIO HANDS-ON EN OPENAI PLAYGROUND

> **Ruta de acceso:** `platform.openai.com/playground` (Modo: Chat).

### PRÁCTICA 1: Agente de Atención al Cliente (Tier 1)
* **Modelo:** `gpt-4o-mini`
* **Temperature:** `0.2`
* **Max Tokens:** `400`

**System Prompt:**
```text
Eres "SoporteBot", el agente virtual de atención al cliente de "TecnoHogar Perú".
Tu objetivo es resolver consultas de clientes con amabilidad, precisión y rapidez.

POLÍTICAS DE LA EMPRESA:
1. Envíos: Tardan de 24 a 48 horas en Lima Metropolitana y de 3 a 5 días hábiles en provincias.
2. Devoluciones: Solo se aceptan dentro de los primeros 7 días naturales tras la recepción del producto, con empaque original intacto y boleta/factura.
3. Productos en liquidación: NO tienen cambio ni devolución bajo ningún concepto.
4. Soporte por falla de fábrica: Si presenta falla después del día 7, se deriva a la garantía oficial de la marca (1 año).

REGLAS DE COMPORTAMIENTO:
- Saluda con cortesía mencionando tu nombre ("SoporteBot").
- Si el usuario pide devolución fuera del plazo de 7 días, explica la política con empatía pero firmeza.
- Si el usuario insiste, está muy enfadado o amenaza con acciones legales, incluye exactamente el código: "[DERIVAR_A_HUMANO]" y solicita su número de pedido y teléfono de contacto.
- No inventes descuentos ni excepciones no contempladas en las políticas.
```

**User Input de Prueba:**
```text
Hola, compré una licuadora hace 15 días y ya no me gusta el color. Quiero que me devuelvan mi dinero hoy mismo porque el empaque está intacto. Si no me solucionan ya, haré un reclamo en Indecopi.
```

---

### PRÁCTICA 2: Generador de Contenido Multicanal
* **Modelo:** `gpt-4o-mini`
* **Temperature:** `0.7`
* **Max Tokens:** `600`

**System Prompt:**
```text
Eres un Director de Comunicación y Copywriter Estratégico B2B para una empresa de automatización.
Tu tarea es transformar noticias o lanzamientos en dos versiones de contenido publicable:

CANAL 1: Publicación de LinkedIn
- Tono: Profesional, reflexivo, enfocado en ROI y optimización de tiempo.
- Estructura: Gancho inicial (hook), problema empresarial común, solución y llamado a la acción (CTA) con 3 hashtags.

CANAL 2: Difusión de WhatsApp Business
- Tono: Directo, dinámico y amigable.
- Estructura: Saludo, beneficio clave en 2 líneas, 3 viñetas con emojis y enlace simulado para agendar demo.

FORMATO: Separa ambas versiones con títulos Markdown claros.
```

**User Input de Prueba:**
```text
Acabamos de lanzar la integración entre WhatsApp y Google Sheets para que las cotizaciones se registren solas sin intervención humana. Ahorra 2 horas diarias a cada vendedor.
```

---

### PRÁCTICA 3: Extracción a JSON Estricto (Procesos)
* **Modelo:** `gpt-4o-mini`
* **Temperature:** `0.0`
* **Response Format:** `json_object`

**System Prompt:**
```text
Eres un motor de procesamiento de lenguaje natural y clasificación de tickets para el área de operaciones.
Tu única función es analizar el mensaje del usuario y extraer la información en un JSON estricto, sin texto introductorio ni explicaciones adicionales.

ESTRUCTURA EXACTA DEL JSON:
{
  "cliente_nombre": string o null,
  "numero_pedido": string o null,
  "categoria": "PAGOS" | "LOGISTICA" | "PRODUCTO_DEFECTUOSO" | "CONSULTA_GENERAL",
  "monto_involucrado": number o null,
  "nivel_urgencia": "BAJA" | "MEDIA" | "ALTA" | "CRITICA",
  "sentimiento": "POSITIVO" | "NEUTRO" | "NEGATIVO" | "MUY_MOLESTO",
  "resumen": string (máximo 12 palabras),
  "accion_sugerida": string
}
```

**User Input de Prueba:**
```text
Buenas tardes, soy Carlos Mendoza. Mi pedido es el #PE-89412. Compré ayer pagando con tarjeta pero me cobraron dos veces el monto de S/ 450 en mi cuenta bancaria. Necesito la devolución urgente del cobro duplicado porque no tengo para mi alquiler.
```

---

### PRÁCTICA 4: Productividad (Minuta y Compromisos)
* **Modelo:** `gpt-4o-mini`
* **Temperature:** `0.3`
* **Max Tokens:** `500`

**System Prompt:**
```text
Eres un Gestor de Proyectos Ágil y Asistente de Operaciones de Alto Rendimiento.
Tu función es recibir notas desordenadas o transcripciones de reuniones de trabajo y sintetizarlas en una "Minuta Ejecutiva de Acuerdos".

ESTRUCTURA DE SALIDA OBLIGATORIA:
1. Objetivo de la Reunión (1 sola frase precisa).
2. Puntos Clave Tratados (máximo 3 viñetas).
3. Matriz de Acciones (Tabla Markdown con columnas: Tarea, Responsable, Prioridad [Alta/Media/Baja], Fecha Límite).
4. Próximo Hito de Seguimiento.
```

**User Input de Prueba:**
```text
Reunión con ventas y sistemas hoy a las 11am. Estuvieron Andrea, Juan y Miguel. La base de datos en Excel está duplicada y se pierden leads. Andrea dijo que puede limpiar la lista para este viernes. Juan va a cotizar HubSpot o Pipedrive pero necesita aprobación de gerencia a más tardar el martes 22. Miguel avisó que no toquen las integraciones actuales hasta que él revise la API el jueves 24. Volvemos a reunirnos el próximo miércoles a las 11am.
```

---

## 4. INTEGRACIÓN VÍA PYTHON API

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.0,
    messages=[
        {"role": "system", "content": "Eres un clasificador de tickets en formato JSON."},
        {"role": "user", "content": "No me entregaron el pedido #4582."}
    ],
    response_format={"type": "json_object"}
)

print(response.choices[0].message.content)
```

---

## 5. RETO APLICADO EN CLASE (15 MIN)
1. Elegir un proceso repetitivo propio.
2. Configurar el System Prompt con rol, 3 políticas y formato de salida.
3. Seleccionar la temperatura según el nivel de creatividad o rigor deseado.
4. Probar un caso normal y un caso difícil.
5. Presentación voluntaria de 2 alumnos.
