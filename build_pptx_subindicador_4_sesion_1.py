import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors (Modern Dark Tech Palette)
    c_bg_dark = RGBColor(15, 23, 42)        # Slate 900
    c_card_bg = RGBColor(30, 41, 59)        # Slate 800
    c_primary = RGBColor(37, 99, 235)       # Blue 600
    c_accent = RGBColor(14, 165, 233)       # Sky 500
    c_accent_green = RGBColor(16, 185, 129) # Emerald 500
    c_accent_amber = RGBColor(245, 158, 11) # Amber 500
    c_text_white = RGBColor(255, 255, 255)
    c_text_muted = RGBColor(148, 163, 184)  # Slate 400
    c_border = RGBColor(51, 65, 85)         # Slate 700

    def add_bg(slide):
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        shape.fill.solid()
        shape.fill.fore_color.rgb = c_bg_dark
        shape.line.fill.background()
        return shape

    def add_header(slide, title_text, category="SUBINDICADOR 4: DISEÑO DE PROMPTS | SESIÓN 1 DE 2"):
        tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.7), Inches(0.4))
        p_cat = tb_cat.text_frame.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(13)
        p_cat.font.bold = True
        p_cat.font.color.rgb = c_accent

        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.85))
        p_title = tb_title.text_frame.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(28)
        p_title.font.bold = True
        p_title.font.color.rgb = c_text_white

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.55), Inches(11.733), Inches(0.025))
        line.fill.solid()
        line.fill.fore_color.rgb = c_border
        line.line.fill.background()

    def add_speaker_note(slide, note_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = note_text

    # =========================================================================
    # SLIDE 1: PORTADA
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)

    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.3), Inches(5.6), Inches(0.55))
    badge.fill.solid()
    badge.fill.fore_color.rgb = c_primary
    badge.line.fill.background()
    p_b = badge.text_frame.paragraphs[0]
    p_b.text = "CURSO: AUTOMATIZACIÓN DE AGENTES DE IA"
    p_b.font.size = Pt(14)
    p_b.font.bold = True
    p_b.font.color.rgb = c_text_white
    p_b.alignment = PP_ALIGN.CENTER

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(2.1), Inches(11.7), Inches(3.2))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "Diseño de Prompts Efectivos para Agentes"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = c_text_white

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "Sesión 1: Estructura Anatómica, Contexto, Delimitadores y Few-Shot Prompting en OpenAI Platform."
    p1_sub.font.size = Pt(22)
    p1_sub.font.color.rgb = c_text_muted
    p1_sub.space_before = Pt(12)

    meta = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.5), Inches(11.7), Inches(1.4))
    meta.fill.solid()
    meta.fill.fore_color.rgb = c_card_bg
    meta.line.color.rgb = c_border
    tf_meta = meta.text_frame
    tf_meta.word_wrap = True
    p_m1 = tf_meta.paragraphs[0]
    p_m1.text = "Subindicador 4 (Clase 1 de 2: Martes)   •   Horario: 19:30 - 21:45 hrs (135 min)"
    p_m1.font.size = Pt(17)
    p_m1.font.bold = True
    p_m1.font.color.rgb = c_accent
    p_m2 = tf_meta.add_paragraph()
    p_m2.text = "Entorno de Práctica: OpenAI Platform Playground (System Instructions & Few-Shot Mode)"
    p_m2.font.size = Pt(15)
    p_m2.font.color.rgb = c_text_white
    p_m2.space_before = Pt(4)

    add_speaker_note(s1, "Iniciar puntuales a las 19:30. Explicar que el Subindicador 4 comprende 2 clases completas (martes y jueves). Hoy nos enfocaremos en la ingeniería de prompts estructural: cómo redactar instrucciones infalibles para agentes profesionales.")

    # =========================================================================
    # SLIDE 2: AGENDA DE LA CLASE DE HOY
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Agenda de la Sesión de Hoy (19:30 - 21:45)")

    agenda_items = [
        ("19:30 - 19:45", "Apertura & Contexto", "De la conversación informal a la ingeniería: El prompt como código fuente del agente."),
        ("19:45 - 20:15", "Los 5 Componentes Clave", "La fórmula R-C-T-R-F: Rol, Contexto, Tarea, Restricciones y Formato."),
        ("20:15 - 20:25", "Delimitadores & Few-Shot", "Uso de Markdown/XML y cómo enseñar con ejemplos de alta fidelidad."),
        ("20:25 - 20:30", "Pausa Activa / Setup", "Sincronización en OpenAI Playground y configuración de parámetros."),
        ("20:30 - 21:20", "Hands-On: 4 Prácticas en Vivo", "Refactorización de prompts reales, delimitación estricta y Few-Shot en Playground."),
        ("21:20 - 21:45", "Reto en Clase y Cierre", "Construcción de prompt autónomo y puente hacia la Sesión 2 del jueves.")
    ]

    for idx, (hor, tit, desc) in enumerate(agenda_items):
        col = idx % 2
        row = idx // 2
        x = Inches(0.8 + col * 5.95)
        y = Inches(1.75 + row * 1.75)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.75), Inches(1.55))
        card.fill.solid()
        card.fill.fore_color.rgb = c_card_bg
        card.line.color.rgb = c_border
        tf = card.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = f"{hor}  •  {tit}"
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = c_accent
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(14)
        p_d.font.color.rgb = c_text_white
        p_d.space_before = Pt(4)

    add_speaker_note(s2, "Recordar a los alumnos la disciplina de tiempos. Tendremos 50 minutos netos de laboratorio práctico con ejercicios reales.")

    # =========================================================================
    # SLIDE 3: ¿POR QUÉ UN PROMPT PARA AGENTES ES DIFERENTE?
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Prompting Conversacional vs. Prompting de Agentes")

    left = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(5.75), Inches(5.1))
    left.fill.solid()
    left.fill.fore_color.rgb = c_card_bg
    left.line.color.rgb = c_border
    tfl = left.text_frame
    tfl.word_wrap = True
    pl = tfl.paragraphs[0]
    pl.text = "Prompting Informal (ChatGPT)"
    pl.font.size = Pt(20)
    pl.font.bold = True
    pl.font.color.rgb = c_accent_amber

    pts_l = [
        "• Enfoque de usuario: 'Hazme un resumen de esto' o 'Dame ideas'.",
        "• Tolera ambigüedad: Si la respuesta no gusta, el humano repregunta.",
        "• Salida impredecible: Texto libre con párrafos de longitud variable.",
        "• Sin consecuencias graves: Si comete un error, el usuario lo corrige en el momento."
    ]
    for p in pts_l:
        par = tfl.add_paragraph()
        par.text = p
        par.font.size = Pt(15)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(14)

    right = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(1.75), Inches(5.75), Inches(5.1))
    right.fill.solid()
    right.fill.fore_color.rgb = c_card_bg
    right.line.color.rgb = c_primary
    tfr = right.text_frame
    tfr.word_wrap = True
    pr = tfr.paragraphs[0]
    pr.text = "Prompting de Agentes (Sistemas de Producción)"
    pr.font.size = Pt(20)
    pr.font.bold = True
    pr.font.color.rgb = c_primary

    pts_r = [
        "• Es el CÓDIGO FUENTE del sistema: Define lógica y reglas de negocio.",
        "• Cero supervisión humana continua: Opera de forma autónoma.",
        "• Salida estricta y determinista: Debe encajar en bases de datos o APIs.",
        "• Manejo de casos de error: Debe saber qué responder cuando faltan datos o el usuario intenta engañarlo."
    ]
    for p in pts_r:
        par = tfr.add_paragraph()
        par.text = p
        par.font.size = Pt(15)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(14)

    add_speaker_note(s3, "Enfatizar que un agente de IA no tiene 'sentido común', solo tiene el System Prompt que nosotros le redactemos.")

    # =========================================================================
    # SLIDE 4: LA FÓRMULA DE LOS 5 COMPONENTES (R-C-T-R-F)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Anatomía de un Prompt Profesional: La Fórmula R-C-T-R-F")

    comps = [
        ("1. ROL / IDENTIDAD", "Quién es el agente, su nivel de experiencia, departamento y perspectiva profesional.", c_primary),
        ("2. CONTEXTO", "El entorno operativo, antecedentes de la empresa, glosario o documentación de soporte.", c_accent),
        ("3. TAREA ESPECÍFICA", "La acción precisa y el objetivo concreto que debe ejecutar paso a paso.", c_accent_green),
        ("4. RESTRICCIONES & GUARDRAILS", "Lo que JAMÁS debe hacer, límites éticos, políticas y qué responder si falta información.", c_accent_amber),
        ("5. FORMATO DE SALIDA", "La estructura final obligatoria: JSON, Tabla Markdown, viñetas delimitadas o campos clave.", c_primary)
    ]

    for idx, (t, d, col) in enumerate(comps):
        y = Inches(1.75 + idx * 1.02)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(0.92))
        card.fill.solid()
        card.fill.fore_color.rgb = c_card_bg
        card.line.color.rgb = col
        card.line.width = Pt(2)
        tf = card.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = t
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = col
        p_d = tf.add_paragraph()
        p_d.text = d
        p_d.font.size = Pt(14)
        p_d.font.color.rgb = c_text_white
        p_d.space_before = Pt(2)

    add_speaker_note(s4, "Decir a los alumnos: Grábense esta fórmula: R-C-T-R-F. Cada vez que construyan un agente para una empresa, deben auditar si tiene estos 5 componentes.")

    # =========================================================================
    # SLIDE 5: EL PODER DE LOS DELIMITADORES
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "Estructuración con Delimitadores: Claridad y Seguridad")

    c_left = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(5.75), Inches(5.1))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = c_card_bg
    c_left.line.color.rgb = c_border
    tf1 = c_left.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "¿Para qué sirven los Delimitadores?"
    p1.font.size = Pt(19)
    p1.font.bold = True
    p1.font.color.rgb = c_accent

    pts_del = [
        "• Separan las instrucciones de los datos: El modelo sabe exactamente qué es una orden y qué es contenido a analizar.",
        "• Previenen Prompt Injections: Si un usuario malicioso escribe 'Olvida las instrucciones anteriores', los delimitadores aíslan su texto.",
        "• Facilitan la lectura y mantenimiento del prompt en equipos de trabajo.",
        "• Delimitadores estándar: ###, \"\"\", ```, o etiquetas XML (<contexto>, <reglas>)."
    ]
    for b in pts_del:
        p = tf1.add_paragraph()
        p.text = b
        p.font.size = Pt(15)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(12)

    c_right = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(1.75), Inches(5.75), Inches(5.1))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = RGBColor(10, 15, 30)
    c_right.line.color.rgb = c_accent_green
    tf2 = c_right.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = "Ejemplo Visual de Estructura Delimitada:"
    p2.font.size = Pt(16)
    p2.font.bold = True
    p2.font.color.rgb = c_accent_green

    code_lines = [
        "### ROL Y OBJETIVO",
        "Eres un analista de créditos...",
        "",
        "### MANUAL DE POLÍTICAS",
        "<politicas>",
        "- Ingreso mínimo: S/ 2,500 netos.",
        "- Máximo endeudamiento: 40%.",
        "</politicas>",
        "",
        "### DATOS DEL CLIENTE",
        '"""',
        "{mensaje_usuario}",
        '"""',
        "",
        "### FORMATO OBLIGATORIO DE RESPUESTA",
        "Genera una tabla con Dictamen y Motivo."
    ]
    for cl in code_lines:
        p = tf2.add_paragraph()
        p.text = cl
        p.font.size = Pt(13)
        p.font.name = "Courier New"
        p.font.color.rgb = RGBColor(226, 232, 240)
        p.space_before = Pt(2)

    add_speaker_note(s5, "Mostrar cómo las etiquetas XML <politicas></politicas> hacen imposible que el LLM confunda una regla con el texto que ingresó un usuario.")

    # =========================================================================
    # SLIDE 6: ZERO-SHOT VS FEW-SHOT PROMPTING
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Técnicas de Instrucción: Zero-Shot vs. Few-Shot")

    card_zs = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(5.75), Inches(5.1))
    card_zs.fill.solid()
    card_zs.fill.fore_color.rgb = c_card_bg
    card_zs.line.color.rgb = c_border
    tf_zs = card_zs.text_frame
    tf_zs.word_wrap = True
    p = tf_zs.paragraphs[0]
    p.text = "Zero-Shot Prompting (Sin Ejemplos)"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = c_accent

    pts_zs = [
        "• Se le pide al modelo resolver la tarea basándose únicamente en su conocimiento previo y las instrucciones dadas.",
        "• Cuándo usarlo: Tareas estándar, redacción general, traducción o resúmenes sencillos.",
        "• Riesgo: El modelo puede interpretar el formato o criterio de clasificación a su propio criterio subjetivo."
    ]
    for pt in pts_zs:
        par = tf_zs.add_paragraph()
        par.text = pt
        par.font.size = Pt(15)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(14)

    card_fs = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(1.75), Inches(5.75), Inches(5.1))
    card_fs.fill.solid()
    card_fs.fill.fore_color.rgb = c_card_bg
    card_fs.line.color.rgb = c_accent_green
    tf_fs = card_fs.text_frame
    tf_fs.word_wrap = True
    p = tf_fs.paragraphs[0]
    p.text = "Few-Shot Prompting (Con Ejemplos)"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = c_accent_green

    pts_fs = [
        "• Se le proporcionan de 2 a 5 ejemplos exactos de 'Entrada -> Salida' antes de pedirle que resuelva el caso real.",
        "• Cuándo usarlo: Clasificaciones ambiguas, formatos de salida ultra estrictos o tono muy corporativo.",
        "• Beneficio: Elimina el 90% de ambigüedades sin necesidad de entrenar o 'fine-tunear' el modelo con código."
    ]
    for pt in pts_fs:
        par = tf_fs.add_paragraph()
        par.text = pt
        par.font.size = Pt(15)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(14)

    add_speaker_note(s6, "La regla de oro: Si el modelo falla en entender tu instrucción explicada con palabras, no agregues más palabras; ponle un ejemplo claro de entrada y salida.")

    # =========================================================================
    # SLIDE 7: CÓMO HACER FEW-SHOT EN OPENAI PLAYGROUND
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "¿Cómo Implementar Few-Shot en OpenAI Playground?")

    items_fs = [
        ("Opción 1: Dentro del System Prompt (En el texto)", "Escribir directamente dentro de la caja de System: 'EJEMPLO 1: Input: ... Output: ...' 'EJEMPLO 2: Input: ... Output: ...'. Es el método más portable para Make/Zapier.", Inches(1.75)),
        ("Opción 2: Usando Mensajes User / Assistant Previos", "En el Playground, hacer clic en '+ Add Message' y simular una conversación previa donde el User pone un caso y el Assistant responde exactamente como queremos.", Inches(3.45)),
        ("El Secreto de la Calidad en Few-Shot", "Los ejemplos deben cubrir casos variados: Un ejemplo estándar positivo, un ejemplo de rechazo o negativo, y un ejemplo de caso incompleto.", Inches(5.15))
    ]

    for title, desc, y_pos in items_fs:
        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y_pos, Inches(11.7), Inches(1.5))
        card.fill.solid()
        card.fill.fore_color.rgb = c_card_bg
        card.line.color.rgb = c_border
        tf = card.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(18)
        p_t.font.bold = True
        p_t.font.color.rgb = c_accent
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(15)
        p_d.font.color.rgb = c_text_white
        p_d.space_before = Pt(4)

    add_speaker_note(s7, "Mostrar en vivo en la pantalla de Playground cómo agregar turnos de conversación para entrenar en contexto al agente.")

    # =========================================================================
    # SLIDE 8: CONTROL DE SALIDAS Y CASOS NEGATIVOS
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "Regla de Oro: Instruir sobre el 'Caso Negativo'")

    c_box1 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(5.75), Inches(5.1))
    c_box1.fill.solid()
    c_box1.fill.fore_color.rgb = c_card_bg
    c_box1.line.color.rgb = c_accent_amber
    tf_c1 = c_box1.text_frame
    tf_c1.word_wrap = True
    p = tf_c1.paragraphs[0]
    p.text = "El Error Típico del Principiante"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = c_accent_amber

    err_pts = [
        "• El principiante solo le dice al agente qué hacer cuando todo está perfecto.",
        "• ¿Qué pasa si el cliente NO envía su número de pedido?",
        "• ¿Qué pasa si el documento adjunto no tiene relación con el tema?",
        "• Resultado: El modelo improvisa, alucina datos falsos o genera un texto incoherente que rompe la automatización."
    ]
    for ep in err_pts:
        par = tf_c1.add_paragraph()
        par.text = ep
        par.font.size = Pt(15)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(12)

    c_box2 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(1.75), Inches(5.75), Inches(5.1))
    c_box2.fill.solid()
    c_box2.fill.fore_color.rgb = c_card_bg
    c_box2.line.color.rgb = c_accent_green
    tf_c2 = c_box2.text_frame
    tf_c2.word_wrap = True
    p = tf_c2.paragraphs[0]
    p.text = "La Práctica del Automatizador Experto"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = c_accent_green

    exp_pts = [
        "• Definir SIEMPRE el comportamiento por defecto:",
        "  'Si el dato X no está presente, devuelve null'.",
        "  'Si la pregunta no está en el manual adjunto, responde exactamente: Lo siento, no cuento con esa información en mi base autorizada'.",
        "• Cero alucinación: Restringir la creatividad a cero (Temperature 0.0) cuando se trata de datos institucionales."
    ]
    for xp in exp_pts:
        par = tf_c2.add_paragraph()
        par.text = xp
        par.font.size = Pt(15)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(12)

    add_speaker_note(s8, "Hacer que los alumnos repitan: 'Si no le digo al agente qué hacer cuando falta información, él inventará la información'.")

    # =========================================================================
    # SLIDE 9: TALLER PRÁCTICO 1 - EL ANTES Y EL DESPUÉS
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "Práctica 1: Deconstrucción de un Mal Prompt vs. Estructurado")

    p1_l = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(5.75), Inches(5.1))
    p1_l.fill.solid()
    p1_l.fill.fore_color.rgb = RGBColor(40, 20, 20)
    p1_l.line.color.rgb = RGBColor(239, 68, 68)
    tf_p1l = p1_l.text_frame
    tf_p1l.word_wrap = True
    p = tf_p1l.paragraphs[0]
    p.text = "❌ Prompt Mal Diseñado (Vago):"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(239, 68, 68)

    p_bad = tf_p1l.add_paragraph()
    p_bad.text = '"Eres un asistente de ventas. Revisa este mensaje de un cliente potencial y dime si vale la pena llamarlo o no y dame sus datos."'
    p_bad.font.size = Pt(15)
    p_bad.font.color.rgb = c_text_white
    p_bad.space_before = Pt(14)

    p_bad_flaws = [
        "• ¿Qué criterios definen si 'vale la pena'?",
        "• ¿En qué formato debe entregar los datos?",
        "• ¿Qué tono debe tener?",
        "• Salida: Un párrafo desordenado inútil para un CRM."
    ]
    for flaw in p_bad_flaws:
        par = tf_p1l.add_paragraph()
        par.text = flaw
        par.font.size = Pt(14)
        par.font.color.rgb = c_text_muted
        par.space_before = Pt(8)

    p1_r = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(1.75), Inches(5.75), Inches(5.1))
    p1_r.fill.solid()
    p1_r.fill.fore_color.rgb = c_card_bg
    p1_r.line.color.rgb = c_accent_green
    tf_p1r = p1_r.text_frame
    tf_p1r.word_wrap = True
    p = tf_p1r.paragraphs[0]
    p.text = "✓ Prompt Refactorizado (R-C-T-R-F):"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = c_accent_green

    p_good_pts = [
        "• Rol: Calificador de Leads B2B para software SaaS.",
        "• Contexto: Empresa vende licencias para equipos > 10 personas.",
        "• Tarea: Evaluar tamaño, presupuesto y urgencia.",
        "• Restricciones: Si no menciona empresa o tamaño, clasificar como 'LEAD TIBIO - REQUIERE INDAGAR'.",
        "• Formato: Objeto JSON con {score_1_al_10, clasificacion, accion_siguiente}."
    ]
    for gpt in p_good_pts:
        par = tf_p1r.add_paragraph()
        par.text = gpt
        par.font.size = Pt(14)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(10)

    add_speaker_note(s9, "Probar ambos en el Playground en vivo para que los alumnos vean la abismal diferencia en el resultado.")

    # =========================================================================
    # SLIDE 10: TALLER PRÁCTICO 2 - GROUNDING Y DELIMITADORES
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "Práctica 2: Base de Conocimiento Delimitada (Grounding)")

    c_p2 = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(11.7), Inches(5.1))
    c_p2.fill.solid()
    c_p2.fill.fore_color.rgb = c_card_bg
    c_p2.line.color.rgb = c_primary
    tf_p2 = c_p2.text_frame
    tf_p2.word_wrap = True
    p = tf_p2.paragraphs[0]
    p.text = "Objetivo: Crear un Agente Estricto de RRHH que NO invente beneficios"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = c_accent

    pts_p2 = [
        "1. Técnica: Envolver el reglamento interno de la empresa en etiquetas <reglamento> ... </reglamento>.",
        "2. Regla Anti-Alucinación: 'Responde ÚNICAMENTE con hechos presentes dentro de las etiquetas <reglamento>. Si un colaborador consulta por un beneficio que no está en el texto (ej. trabajo remoto o vales de almuerzo), responde: Este beneficio no se encuentra estipulado en la normativa actual.'",
        "3. Parámetro Técnico: Temperature = 0.0 (Cero creatividad).",
        "4. Caso de Prueba en Vivo: El usuario pregunta: '¿Puedo pedir viernes de home office si ya terminé mis tareas?'.",
        "5. Resultado esperado: Rechazo educado basado 100% en el texto delimitado."
    ]
    for pt in pts_p2:
        par = tf_p2.add_paragraph()
        par.text = pt
        par.font.size = Pt(15)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(12)

    add_speaker_note(s10, "Esta práctica es vital para empresas que tienen miedo de que la IA le diga a un cliente o empleado cosas que no son verdad.")

    # =========================================================================
    # SLIDE 11: TALLER PRÁCTICO 3 - FEW-SHOT EN VIVO
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11)
    add_header(s11, "Práctica 3: Few-Shot para Normalización de Catálogo")

    c_p3_l = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(5.75), Inches(5.1))
    c_p3_l.fill.solid()
    c_p3_l.fill.fore_color.rgb = c_card_bg
    c_p3_l.line.color.rgb = c_accent_green
    tf_p3l = c_p3_l.text_frame
    tf_p3l.word_wrap = True
    p = tf_p3l.paragraphs[0]
    p.text = "El Desafío: Datos Sucios de Proveedores"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = c_accent_green

    pts_p3l = [
        "• Cada vendedor o proveedor sube títulos como:",
        "  'laptop lenov thinkpd i7 16gb remate!!!'",
        "  'TELEVISOR SAMSUNG 55 PULG 4K SMART TV MODELO 2026'",
        "• Necesitamos un formato canónico estricto para el sistema de inventario:",
        "  [MARCA] | [TIPO] | [ESPECIFICACIONES PRINCIPALES]"
    ]
    for pt in pts_p3l:
        par = tf_p3l.add_paragraph()
        par.text = pt
        par.font.size = Pt(14.5)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(12)

    c_p3_r = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(1.75), Inches(5.75), Inches(5.1))
    c_p3_r.fill.solid()
    c_p3_r.fill.fore_color.rgb = RGBColor(10, 15, 30)
    c_p3_r.line.color.rgb = c_accent
    tf_p3r = c_p3_r.text_frame
    tf_p3r.word_wrap = True
    p = tf_p3r.paragraphs[0]
    p.text = "Inyección de 2 Ejemplos en el Prompt:"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = c_accent

    ex_code = [
        "### EJEMPLOS CANÓNICOS:",
        "Entrada: 'celular xiaomi redmi note 12 128gb azul'",
        "Salida: XIAOMI | Smartphone | Redmi Note 12 - 128GB (Azul)",
        "",
        "Entrada: 'impresora epson ecotank l3250 wifi multifuncional'",
        "Salida: EPSON | Impresora Multifuncional | EcoTank L3250 (WiFi)",
        "",
        "### CASO A PROCESAR:",
        "Entrada: 'audifonos inalambricos sony wh-1000xm5 negro cancelacion ruido'",
        "Salida: ???"
    ]
    for ec in ex_code:
        par = tf_p3r.add_paragraph()
        par.text = ec
        par.font.size = Pt(12)
        par.font.name = "Courier New"
        par.font.color.rgb = RGBColor(226, 232, 240)
        par.space_before = Pt(2)

    add_speaker_note(s11, "Hacer la prueba en Playground. Verán cómo el modelo infiere el patrón exacto sin titubear.")

    # =========================================================================
    # SLIDE 12: TALLER PRÁCTICO 4 - FORMATO ESTRICTO DE AUDITORÍA
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12)
    add_header(s12, "Práctica 4: Auditor de Calidad con Evaluación Objetiva")

    c_p4 = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(11.7), Inches(5.1))
    c_p4.fill.solid()
    c_p4.fill.fore_color.rgb = c_card_bg
    c_p4.line.color.rgb = c_primary
    tf_p4 = c_p4.text_frame
    tf_p4.word_wrap = True
    p = tf_p4.paragraphs[0]
    p.text = "Agente de Calidad (QA) para Conversaciones de Soporte"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = c_primary

    pts_p4 = [
        "• Rol: Auditor de Calidad y Cumplimiento de Procesos de Call Center.",
        "• Tarea: Evaluar la transcripción entre un asesor y un cliente.",
        "• Criterios Cuantitativos Estrictos:",
        "  1. ¿Saludó según el protocolo de la empresa? (0 a 20 pts).",
        "  2. ¿Validó la identidad del titular antes de brindar información? (0 o 40 pts - Eliminatorio).",
        "  3. ¿Ofreció solución en el primer contacto sin rodeos? (0 a 20 pts).",
        "  4. ¿Despedida cordial y encuesta? (0 a 20 pts).",
        "• Formato de Salida: Tabla con desglose de puntaje + Nota Final (0-100) + Veredicto: [APROBADO / OBSERVADO]."
    ]
    for pt in pts_p4:
        par = tf_p4.add_paragraph()
        par.text = pt
        par.font.size = Pt(15)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(10)

    add_speaker_note(s12, "Destacar que convertir evaluaciones cualitativas en rúbricas cuantitativas estructuradas es uno de los servicios más rentables para consultores de IA.")

    # =========================================================================
    # SLIDE 13: RETO APLICADO EN CLASE (15 MIN)
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_bg(s13)
    add_header(s13, "Reto en Clase: Refactoriza un Prompt Real (15 minutos)")

    r_card = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(11.7), Inches(5.1))
    r_card.fill.solid()
    r_card.fill.fore_color.rgb = c_card_bg
    r_card.line.color.rgb = c_accent
    tf_r = r_card.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "Dinámica Individual / Parejas:"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = c_accent

    steps = [
        "1. Toma una tarea cotidiana de tu empresa (ej. redactar emails de cobranza, filtrar reclamos, calificar postulantes a un puesto).",
        "2. Aplica la estructura R-C-T-R-F de forma explícita en OpenAI Playground.",
        "3. Incorpora al menos 1 delimitador (### o XML tags) y 1 regla explícita de 'caso negativo' (qué hacer si faltan datos).",
        "4. Incluye 2 ejemplos Few-Shot si tu tarea requiere un formato específico.",
        "5. Socialización: 2 alumnos voluntarios proyectarán su Playground para revisión y feedback en vivo."
    ]
    for st in steps:
        par = tf_r.add_paragraph()
        par.text = st
        par.font.size = Pt(16)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(14)

    add_speaker_note(s13, "Dar 10 minutos para desarrollo individual y 5 minutos para que 2 alumnos compartan pantalla.")

    # =========================================================================
    # SLIDE 14: CONCLUSIONES Y ADELANTO SESIÓN 2 (JUEVES)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_bg(s14)
    add_header(s14, "Conclusiones y Conexión con la Sesión del Jueves")

    c1 = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(5.75), Inches(5.1))
    c1.fill.solid()
    c1.fill.fore_color.rgb = c_card_bg
    c1.line.color.rgb = c_border
    tfc1 = c1.text_frame
    tfc1.word_wrap = True
    p = tfc1.paragraphs[0]
    p.text = "Lo Aprendido Hoy (Sesión 1/2)"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = c_accent_green

    pts_fin = [
        "✓ El prompt de un agente no es una conversación: es una especificación de software.",
        "✓ La fórmula R-C-T-R-F garantiza predictibilidad y elimina ambigüedades.",
        "✓ Los delimitadores protegen al agente contra inyecciones y separan datos de órdenes.",
        "✓ Few-Shot Prompting es la forma más rápida de lograr precisión quirúrgica sin programar."
    ]
    for pf in pts_fin:
        par = tfc1.add_paragraph()
        par.text = pf
        par.font.size = Pt(15)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(12)

    c2 = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(1.75), Inches(5.75), Inches(5.1))
    c2.fill.solid()
    c2.fill.fore_color.rgb = c_card_bg
    c2.line.color.rgb = c_border
    tfc2 = c2.text_frame
    tfc2.word_wrap = True
    p = tfc2.paragraphs[0]
    p.text = "Próxima Clase (Jueves - Sesión 2/2)"
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = c_primary

    pts_next = [
        "• Técnicas Avanzadas de Razonamiento: Chain-of-Thought (CoT) y razonamiento paso a paso.",
        "• Blindaje y Hardening contra Prompt Injection malicioso.",
        "• Optimización de Costos y Tokens para producción.",
        "• Iteración y Evaluación Sistemática de Prompts con métricas de acierto.",
        "• ¡Nos vemos el jueves a las 19:30!"
    ]
    for pn in pts_next:
        par = tfc2.add_paragraph()
        par.text = pn
        par.font.size = Pt(15)
        par.font.color.rgb = c_text_white
        par.space_before = Pt(12)

    add_speaker_note(s14, "Cerrar puntuales a las 21:45 felicitando al grupo por el avance en la creación de prompts estructurados.")

    output_path = "/Users/rpineda/Sources/Automatizacion/Sesion_1_Subindicador_4_Automatizacion_IA.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    create_deck()
