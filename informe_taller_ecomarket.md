# Informe del Taller Práctico #1  
## Caso de estudio: Optimización de la atención al cliente en EcoMarket

**Estudiante:**  
**Curso:**  
**Repositorio de GitHub:** 

## Presentación del problema

EcoMarket es una empresa de comercio electrónico orientada a la venta de productos sostenibles. El caso plantea un escenario de crecimiento acelerado en el que el área de atención al cliente se convierte en un cuello de botella: la empresa recibe miles de consultas por múltiples canales, el 80% de ellas son repetitivas y el 20% restante exige juicio, empatía y manejo cuidadoso del contexto. En este tipo de situaciones, una solución de inteligencia artificial no debe pensarse solo como una herramienta de automatización, sino como una arquitectura sociotécnica capaz de equilibrar precisión operativa, calidad conversacional, seguridad y supervisión humana.

La propuesta desarrollada en este repositorio parte de una idea central: **no conviene delegar toda la atención al cliente a un modelo generativo aislado**. Los modelos de lenguaje actuales son potentes porque se apoyan en arquitecturas tipo *Transformer*, una familia de modelos basada en mecanismos de atención que permitió escalar notablemente la generación y comprensión de texto (Vaswani et al., 2017). Sin embargo, en contextos empresariales sensibles, especialmente cuando se manejan pedidos, devoluciones y datos personales, un modelo generativo por sí solo puede cometer errores, inventar información o responder sin suficiente trazabilidad. Por eso, el diseño implementado en el código combina generación de lenguaje, datos estructurados, reglas de negocio y posibilidad de escalamiento humano, siguiendo una lógica alineada con enfoques contemporáneos de IA confiable y gestión de riesgos (Autio et al., 2024; OECD, n.d.).

## Fase 1. Selección y justificación del modelo de IA

### 1.1. Modelo seleccionado

La solución propuesta utiliza como núcleo generativo el modelo **`Qwen/Qwen2.5-0.5B-Instruct`**, cargado mediante la librería `transformers`. Según la tarjeta técnica del modelo, esta variante es un modelo causal ajustado para instrucciones, con aproximadamente **0.49 mil millones de parámetros**, diseñado para seguir instrucciones, trabajar con salidas estructuradas y funcionar en escenarios conversacionales (Qwen, n.d.). Desde el punto de vista técnico, esto lo hace adecuado para un ejercicio académico en el que se requiere demostrar cómo el diseño del *prompt* modifica la calidad de la respuesta, sin depender de una infraestructura costosa o de servicios cerrados.

En el código, esta elección aparece en la clase `MotorGenerativoEcoMarket`, donde el atributo `nombre_modelo` se inicializa como `"Qwen/Qwen2.5-0.5B-Instruct"`. Esta decisión no es accidental. El taller no exige entrenar un modelo desde cero ni desplegar una solución empresarial a escala real, sino justificar una selección coherente con el problema y luego evidenciar, en código, el efecto de la ingeniería de *prompts*. En este contexto, un modelo *instruct* pequeño y abierto es una elección razonable porque permite trabajar con inferencia local o semilocal, reduce barreras de acceso y hace visible la relación entre contexto, reglas y salida generada.

### 1.2. ¿Por qué este modelo y no otro?

La justificación no depende de una sola variable. Se apoya en cinco criterios: arquitectura, costo, escalabilidad, integración y calidad esperada de la respuesta.

#### a) Arquitectura adecuada para generación de texto

Los modelos de lenguaje actuales heredan la lógica del *Transformer*, una arquitectura que sustituyó recurrencia y convolución por mecanismos de atención, logrando gran capacidad de paralelización y desempeño en tareas secuenciales complejas (Vaswani et al., 2017). Esto hace posible que modelos como Qwen puedan producir respuestas naturales, contextualizadas y relativamente coherentes para tareas como atención al cliente, redacción de mensajes o reformulación de información estructurada.

Ahora bien, la sola capacidad de generar texto no basta. El código del proyecto reconoce esto y evita usar el modelo como “oráculo”. En lugar de preguntarle libremente al sistema por el estado de un pedido o por una política de devolución, primero construye contexto explícito a partir de datos verificados. De esa manera, el modelo no resuelve la consulta “desde memoria”, sino que redacta una respuesta a partir de una base controlada.

#### b) Relación costo–desempeño

En aplicaciones reales existe una tensión constante entre capacidad del modelo y costo operativo. La documentación de *prompt engineering* de OpenAI resume bien ese principio al indicar que los modelos grandes y pequeños implican compensaciones entre velocidad, costo e inteligencia; los más pequeños suelen ser más rápidos y baratos, mientras los más grandes tienden a resolver mejor problemas más complejos (OpenAI, n.d.). En este proyecto, esa tensión se resuelve con una estrategia práctica: elegir un modelo pequeño para reducir costo y complejidad, y compensar sus limitaciones mediante reglas de negocio, datos estructurados y diseño de *prompts*.

En otras palabras, en lugar de intentar que el modelo “sepa todo”, la arquitectura hace que el sistema **dependa menos del tamaño del modelo y más de la calidad del contexto entregado**. Esto es especialmente apropiado para EcoMarket, donde la mayoría de las consultas son repetitivas y están asociadas a información que ya existe en registros formales.

#### c) Escalabilidad operativa

La empresa reporta que aproximadamente el 80% de las consultas son repetitivas. Esto sugiere que una automatización parcial podría producir una mejora significativa en tiempos de respuesta. La propuesta implementada permite precisamente eso: automatizar casos rutinarios, como consulta de pedidos y orientación sobre devoluciones, y reservar los casos complejos para revisión humana. Este criterio coincide con la idea de una IA confiable y humana en el centro, donde la automatización se aplica de forma contextual y no indiscriminada (OECD, n.d.).

Además, la solución es escalable porque la lógica no depende de un único tipo de consulta. La estructura puede ampliarse fácilmente para incorporar nuevas intenciones, como preguntas sobre características del producto, cambios de dirección, cancelaciones o recomendaciones de compra. Basta con ampliar las fuentes de contexto y las funciones de validación.

#### d) Facilidad de integración

La librería `transformers` de Hugging Face proporciona soporte para inferencia con modelos preentrenados y tareas de generación de texto, lo que facilita la integración del modelo con aplicaciones escritas en Python (Hugging Face, n.d.-a). En el código del taller esto se observa con claridad: el modelo y el tokenizador se cargan con `AutoTokenizer.from_pretrained(...)` y `AutoModelForCausalLM.from_pretrained(...)`, y luego se ejecuta la generación mediante `model.generate(...)`.

Esa facilidad de integración importa porque una solución empresarial no solo necesita “funcionar”, sino poder conectarse con repositorios de datos, catálogos, políticas, registros de clientes y capas de validación. En este proyecto, la integración se demuestra con estructuras simples en formato JSON y listas de diccionarios, pero la lógica es perfectamente extrapolable a una base de datos SQL, un ERP, un CRM o una API logística.

#### e) Calidad de la respuesta esperada

La calidad no depende exclusivamente del modelo. La guía oficial de *prompt engineering* de OpenAI define esta práctica como el proceso de escribir instrucciones efectivas para obtener salidas consistentes y útiles, y recomienda fijar versiones, usar roles claros y construir evaluaciones para medir el comportamiento del sistema (OpenAI, n.d.). El código del proyecto aplica exactamente esa lógica: no se limita a una pregunta ambigua como “Dame el estado del pedido 12345”, sino que añade reglas, rol, contexto recuperado y formato de salida esperado.

Por tanto, la calidad final no proviene de una “magia” del modelo, sino de la interacción entre tres componentes: **modelo generativo, datos estructurados y *prompt* bien diseñado**. Esa es, precisamente, una de las ideas centrales que el taller busca evidenciar.

### 1.3. Tipo de solución: una arquitectura híbrida

Aunque el núcleo generativo es Qwen, la solución completa no debe describirse como “solo un LLM”. La formulación más precisa es que se trata de una **arquitectura híbrida de generación condicionada por datos y reglas**.

En términos funcionales, el flujo del sistema puede describirse así:

1. El usuario formula una consulta.
2. El sistema identifica la intención general: pedido o devolución.
3. Se consulta la base estructurada pertinente.
4. Se ejecutan validaciones de negocio cuando corresponde.
5. Se construye un *prompt* con rol, restricciones y contexto.
6. El modelo redacta la respuesta.
7. Si hay fallo técnico o ausencia de modelo, se activa una respuesta de respaldo.
8. Si el caso excede las reglas o presenta ambigüedad alta, se recomienda escalar a un agente humano.

Este enfoque se parece a lo que, en un contexto más avanzado, podría evolucionar hacia una estrategia de *retrieval-augmented generation* o de *tool use*: el modelo no “posee” toda la verdad del negocio, sino que la consulta en tiempo de ejecución y luego la expresa en lenguaje natural. Aunque el código no implementa una base vectorial ni una búsqueda semántica formal, sí reproduce el principio esencial: **primero recuperar o validar información; después generar**.

### 1.4. Justificación específica con base en el código entregado

El código muestra una decisión metodológica consistente con la necesidad del caso:

- `cargar_base_pedidos()` construye un conjunto de pedidos con estados, fechas, transportadora y motivo de retraso.
- `cargar_politicas_devolucion()` define reglas claras para categorías como accesorios, alimentos, textiles o cuidado personal.
- `evaluar_devolucion(...)` actúa como una capa explícita de validación empresarial.
- `construir_prompt_mejorado_pedido(...)` y `construir_prompt_mejorado_devolucion(...)` convierten la consulta en una instrucción controlada.
- `MotorGenerativoEcoMarket` encapsula la interacción con el modelo.
- `construir_respuesta_respaldo_pedido(...)` y `construir_respuesta_respaldo_devolucion(...)` garantizan continuidad operativa incluso si el modelo no carga.

Este último punto es especialmente importante. En un entorno real, una solución robusta no puede depender completamente de que el modelo esté siempre disponible. El hecho de que el programa tenga un **modo de respaldo** aumenta la confiabilidad del sistema y demuestra madurez en el diseño. En vez de interrumpir el servicio, la aplicación responde con una salida estructurada basada en la misma información validada. Desde la perspectiva de negocio, eso reduce riesgo operativo y mejora continuidad del servicio.

### 1.5. Decisión final para la fase 1

La selección del modelo y la arquitectura se justifica así: **para EcoMarket conviene una solución híbrida compuesta por un modelo open-source ajustado para instrucciones, conectado a datos estructurados y reforzado con reglas de negocio y escalamiento humano**. No se trata de elegir el modelo “más poderoso” en abstracto, sino el más adecuado para el problema concreto. Dado que la mayoría de consultas son repetitivas y verificables, el modelo no necesita razonar libremente sobre conocimiento desconocido; necesita, sobre todo, redactar con claridad, seguir instrucciones y respetar el contexto suministrado.

## Fase 2. Evaluación de fortalezas, limitaciones y riesgos éticos

### 2.1. Fortalezas de la solución propuesta

La principal fortaleza del sistema es que **reduce el tiempo de respuesta** en las consultas repetitivas. En el caso planteado, donde el tiempo promedio actual es de 24 horas, automatizar una fracción importante del 80% de consultas recurrentes permitiría ofrecer respuestas inmediatas o casi inmediatas. Esto mejora la experiencia del cliente y libera tiempo del equipo humano para casos sensibles.

Otra fortaleza es la **consistencia discursiva**. El sistema siempre puede responder usando un tono definido, una estructura clara y restricciones de contenido. Esto es visible en los *prompts* mejorados, que obligan al modelo a hablar como un agente amable, a no inventar información, a incluir fecha estimada y a disculparse si hay retraso. En servicio al cliente, esta consistencia tiene valor porque reduce ambigüedades y hace que el usuario perciba estabilidad en la atención.

La tercera fortaleza es la **trazabilidad parcial**. Aunque el sistema usa generación de lenguaje, la información de base procede de estructuras controladas: pedidos, políticas y catálogo. Esto hace que las respuestas no dependan solamente de conocimiento general del modelo. En términos de gobernanza, esta decisión es más segura que permitir respuestas libres sobre datos empresariales críticos.

La cuarta fortaleza es la **modularidad**. El código está organizado por funciones, lo que facilita mantenimiento, extensión y auditoría. La lógica de consulta de pedidos, la lógica de devolución, la carga del modelo y la interfaz están separadas. Esta separación de responsabilidades es deseable en proyectos de IA aplicada porque permite probar componentes individualmente y mejorar unos sin reescribir todo el sistema.

Finalmente, la solución tiene una fortaleza pedagógica notable: **demuestra de manera visible el impacto de la ingeniería de *prompts***. El usuario puede comparar *prompts* básicos y mejorados para el mismo problema, y observar que la diferencia en rol, contexto y reglas produce respuestas más útiles. Eso se alinea de forma directa con la intención del taller.

### 2.2. Limitaciones técnicas y operativas

La primera limitación es evidente: **el sistema no resuelve bien el 20% de casos complejos por sí solo**. Una queja sensible, una disputa por cobro, un error emocionalmente delicado o una sugerencia extensa no pueden reducirse a datos estructurados ni a reglas simples. Aquí la empatía humana, el criterio contextual y la flexibilidad conversacional siguen siendo indispensables.

La segunda limitación es el **tamaño y capacidad del modelo**. El modelo usado en el proyecto es útil para demostración y para tareas acotadas, pero no debe asumirse como equivalente a modelos de mayor tamaño en comprensión profunda, robustez o razonamiento complejo. El propio campo de *prompt engineering* reconoce que existe un intercambio entre velocidad, costo y capacidad del modelo (OpenAI, n.d.). Por eso, el sistema funciona mejor cuando el problema está bien delimitado y el contexto llega limpio y estructurado.

La tercera limitación es la **dependencia de la calidad de los datos**. Si un pedido está mal registrado, si la fecha de entrega es incorrecta o si una política de devolución está desactualizada, el modelo responderá con elegancia, pero no con verdad. En otras palabras, la generación de lenguaje no corrige errores de la base; solo los expresa de forma persuasiva. Esta es una limitación central en sistemas empresariales basados en IA.

La cuarta limitación es que el prototipo todavía usa una **base de datos simulada** en memoria. Eso es completamente válido para el taller, pero en un entorno real harían falta autenticación, persistencia, control de acceso, logs, mecanismos de actualización y manejo de concurrencia. El sistema demuestra bien el principio, pero no constituye todavía un despliegue productivo.

La quinta limitación es que la clasificación de intenciones no está automatizada en esta versión. El menú obliga al usuario a escoger entre pedido y devolución. En una implementación más realista habría que incorporar un clasificador de intención o una capa adicional que decida automáticamente el flujo de atención.

### 2.3. Riesgos éticos

#### 2.3.1. Alucinaciones

Uno de los riesgos más conocidos de la IA generativa es la generación de contenido plausible pero incorrecto. NIST destaca que la gestión de riesgos en IA generativa debe considerar la confiabilidad y la incorporación sistemática de consideraciones de confianza a lo largo del ciclo de vida del sistema (Autio et al., 2024). En el caso de EcoMarket, una alucinación puede traducirse en algo muy concreto: inventar una fecha de entrega, prometer un reembolso inexistente o afirmar que un producto sí admite devolución cuando en realidad está excluido.

El código mitiga este riesgo de una forma adecuada para el taller. Primero, los *prompts* mejorados incluyen instrucciones explícitas como “No inventes datos que no aparezcan en el contexto”. Segundo, antes de pedirle algo al modelo, el sistema construye un documento estructurado con la información de pedidos o políticas. Tercero, en devoluciones existe una función previa de validación (`evaluar_devolucion`) que reduce el espacio de improvisación. Aun así, el riesgo no desaparece por completo: un modelo puede desobedecer parcialmente una instrucción o responder de forma ambigua. Por eso, en un sistema real convendría añadir validaciones posteriores, pruebas automáticas y registros de auditoría.

#### 2.3.2. Sesgo

La OECD sostiene que una IA confiable debe respetar derechos humanos, valores democráticos, no discriminación, diversidad, equidad y privacidad a lo largo de su ciclo de vida (OECD, n.d.). En servicio al cliente, el sesgo puede emerger de maneras sutiles: distintos niveles de cortesía según la redacción del usuario, peor tratamiento a clientes que escriben con errores ortográficos, respuestas menos claras a usuarios de ciertos contextos lingüísticos o trato desigual en escenarios ambiguos.

En el prototipo, el sesgo no se elimina solo por usar un modelo abierto o pequeño. El modelo sigue estando entrenado con grandes volúmenes de texto y puede heredar patrones no deseados. La mitigación razonable pasa por varias acciones: diseñar *prompts* neutrales, probar con perfiles diversos de usuarios, revisar salidas en casos sensibles y garantizar intervención humana cuando una respuesta pueda afectar derechos o intereses importantes del cliente.

#### 2.3.3. Privacidad y protección de datos

Este es uno de los riesgos más relevantes para un entorno real. Las consultas sobre pedidos suelen involucrar nombres, direcciones, historial de compra, números de seguimiento y, potencialmente, medios de pago. La OECD incluye explícitamente la privacidad y la protección de datos dentro de los principios de IA confiable (OECD, n.d.). NIST, por su parte, insiste en que la gestión de riesgos de IA debe contemplar efectos sobre individuos, organizaciones y sociedad (Autio et al., 2024).

El código del taller usa datos ficticios, lo cual es correcto para un ejercicio académico. Sin embargo, si EcoMarket implementara algo similar en producción, debería aplicar minimización de datos, segmentación de accesos, cifrado, controles de registro y políticas de retención. También sería recomendable que el *prompt* reciba solo la información estrictamente necesaria para responder. No tendría sentido exponer todo el historial de compra si la consulta solo requiere estado del pedido y fecha estimada de entrega.

#### 2.3.4. Transparencia y explicabilidad

La OECD señala que los actores de IA deben comprometerse con transparencia y divulgación responsable, suministrando información significativa sobre capacidades y limitaciones del sistema y, cuando sea útil, sobre las fuentes de datos y la lógica que condujo al resultado (OECD, n.d.). En atención al cliente, esto significa que el usuario no debería creer que está recibiendo una verdad absoluta producida por un sistema infalible.

En la solución propuesta, la transparencia puede fortalecerse de varias maneras: indicar que la respuesta fue generada automáticamente, explicar cuando se usa información del sistema de pedidos y aclarar cuándo un caso será derivado a un agente humano. El prototipo todavía no imprime una etiqueta explícita de “respuesta generada por IA”, pero el diseño sí contempla restricciones y escalamiento. En una versión final, esa transparencia debería hacerse visible para el usuario.

#### 2.3.5. Impacto laboral

El debate sobre IA y trabajo no puede ignorarse. La OECD advierte que la adopción de IA en el trabajo trae beneficios, pero también riesgos asociados con automatización, intensidad del trabajo, recolección de datos, desigualdad y falta de supervisión humana (OECD, 2024). La OIT, además, muestra que la exposición ocupacional a la IA generativa no implica necesariamente desaparición completa de los empleos, sino transformación de tareas, lo que exige diálogo social y políticas de transición (Gmyrek et al., 2025).

Aplicado a EcoMarket, esto significa que el objetivo de la solución no debería ser despedir agentes, sino **redefinir su rol**. Los agentes humanos pueden asumir funciones de mayor valor: resolver excepciones, atender conflictos, supervisar salidas del sistema, actualizar políticas, entrenar nuevas reglas y gestionar casos emocionalmente complejos. Una implementación responsable sería, por tanto, una estrategia de ampliación de capacidades humanas y no de sustitución ciega.

### 2.4. Medidas de mitigación recomendadas

A partir de los riesgos anteriores, se proponen las siguientes medidas:

1. **Base de datos verificada y actualizada.**  
   El sistema generativo solo es tan confiable como la fuente que alimenta el contexto.

2. **Reglas de negocio previas a la generación.**  
   La función `evaluar_devolucion(...)` es un buen comienzo y debería ampliarse a otros procesos.

3. **Restricciones explícitas en los *prompts*.**  
   El código ya hace esto al prohibir la invención de datos y exigir formatos concretos.

4. **Respuestas de respaldo determinísticas.**  
   El modo de respaldo mejora continuidad y reduce dependencia total del modelo.

5. **Escalamiento humano obligatorio en casos complejos o ambiguos.**  
   Esto es clave para preservar empatía, justicia y legitimidad del servicio.

6. **Auditoría y evaluación continua.**  
   La guía de *prompt engineering* recomienda construir evaluaciones para monitorear el comportamiento de las instrucciones y detectar degradación del desempeño (OpenAI, n.d.).

7. **Política de privacidad y minimización de datos.**  
   Solo deben exponerse al modelo los datos necesarios para responder.

8. **Comunicación transparente con el usuario.**  
   Debe explicarse cuándo responde la IA y cuándo interviene un humano.

## Fase 3. Aplicación de principios de ingeniería de prompts

### 3.1. Idea general de la fase práctica

La tercera fase del taller no consiste simplemente en “hacer preguntas al modelo”, sino en demostrar que la calidad de una respuesta depende de cómo se estructura la instrucción. La guía oficial de OpenAI explica que el *prompt engineering* busca obtener salidas consistentes y útiles a través de instrucciones eficaces, y recomienda usar roles, formatos, restricciones y evaluación iterativa (OpenAI, n.d.). El código entregado demuestra exactamente ese principio con dos ejercicios: consulta del estado de un pedido y orientación para devolución de producto.

### 3.2. Cómo está implementada la fase 3 en el código

La fase práctica del proyecto se apoya en cuatro bloques:

#### a) Contexto de datos

La aplicación crea tres fuentes principales de contexto:

- `cargar_base_pedidos()`
- `cargar_politicas_devolucion()`
- `cargar_catalogo_productos()`

Esto permite que los *prompts* no trabajen “en vacío”. En vez de pedirle al modelo que improvise, el programa genera un documento textual con al menos 10 pedidos y otro con las políticas de devolución. Ese diseño responde directamente a la exigencia del taller.

#### b) Validación previa

El caso de devoluciones no se delega enteramente al modelo. Antes de construir el *prompt*, el programa llama a `evaluar_devolucion(...)`. Esta función revisa:

- si la categoría existe,
- si admite devolución,
- el plazo máximo,
- si requiere empaque original,
- y si procede cambio por defecto.

Este punto es muy fuerte desde la perspectiva académica, porque muestra que la ingeniería de *prompts* no reemplaza la lógica de negocio; la complementa.

#### c) Comparación entre *prompt* básico y *prompt* mejorado

El proyecto incluye funciones explícitas para comparar ambos niveles de calidad:

- `construir_prompt_basico_pedido(...)`
- `construir_prompt_mejorado_pedido(...)`
- `construir_prompt_basico_devolucion(...)`
- `construir_prompt_mejorado_devolucion(...)`

Aquí aparece una enseñanza central del taller. Un *prompt* básico suele ser corto, ambiguo y poco restrictivo. Un *prompt* mejorado define rol, límites, objetivos, formato y contexto. Esa diferencia reduce la probabilidad de respuestas incompletas o erróneas.

#### d) Generación y respaldo

La clase `MotorGenerativoEcoMarket` intenta cargar el modelo. Si lo logra, genera una salida con `generate(...)`. Si no, activa un modo de respaldo. Pedagógicamente esto es valioso porque evita que el proyecto dependa completamente del entorno técnico. A nivel conceptual, también refuerza la idea de robustez operacional.

### 3.3. Análisis del prompt de pedido

#### Prompt básico

El *prompt* básico para pedidos tiene la forma:

> “Dame el estado del pedido X usando esta información...”

Este tipo de instrucción tiene una ventaja: es simple. Pero también tiene varias debilidades. No define rol, no fija tono, no ordena qué hacer si falta el pedido, no exige disculpa en caso de retraso y no obliga a incluir fecha ni enlace. En consecuencia, deja demasiado margen de decisión al modelo.

#### Prompt mejorado

El *prompt* mejorado cambia radicalmente la situación. Incluye:

- rol: agente amable, claro y profesional;
- tarea específica: responder una consulta de estado de pedido;
- reglas obligatorias;
- prohibición explícita de inventar información;
- comportamiento en caso de inexistencia del pedido;
- comportamiento en caso de retraso;
- exigencia de incluir fecha estimada y enlace;
- idioma de respuesta;
- formato sugerido de salida.

Además de eso, el *prompt* no solo aporta el documento global de pedidos, sino el **registro identificado** del pedido consultado. Esta redundancia es útil: permite al modelo ver el contexto general y, al mismo tiempo, enfocar la información prioritaria. Desde la perspectiva de ingeniería de *prompts*, esto mejora precisión, reduce dispersión y orienta la atención del modelo hacia el dato verdaderamente relevante.

### 3.4. Análisis del prompt de devolución

#### Prompt básico

El *prompt* básico pregunta si se puede devolver un producto dada una categoría y unas políticas. Su principal problema es que no especifica cómo responder si la devolución no es posible, ni qué hacer con casos de defecto, ni qué tono mantener frente a una negativa.

#### Prompt mejorado

El *prompt* mejorado incorpora elementos cruciales:

- rol empático y profesional;
- uso exclusivo del documento de políticas y de la evaluación previa;
- prohibición de inventar políticas;
- exigencia de claridad cuando la devolución no es posible;
- inclusión de alternativas como revisión manual o cambio por defecto;
- datos del caso concretos;
- formato de respuesta sugerido.

Esta estructura muestra una comprensión adecuada de la rúbrica: no se trata solo de escribir un texto más largo, sino de diseñar una instrucción con **contexto, restricciones, empatía y formato**. En escenarios empresariales reales, este tipo de *prompt* reduce errores reputacionales. Una negativa seca puede irritar al cliente; una negativa explicada con empatía y alternativa de acción mejora la experiencia incluso cuando la empresa no puede conceder la devolución.

### 3.5. ¿Por qué los prompts mejorados son superiores?

Los *prompts* mejorados del proyecto son superiores porque integran cinco principios de diseño:

1. **Definición de rol.**  
   El modelo deja de ser un generador genérico y pasa a actuar como agente de servicio.

2. **Anclaje en contexto.**  
   Se aportan documentos y registros concretos.

3. **Restricción de comportamiento.**  
   Se prohíbe inventar datos y se especifica cómo actuar en excepciones.

4. **Estructuración de salida.**  
   Se indica qué elementos debe contener la respuesta.

5. **Control de tono.**  
   Se exige amabilidad, claridad y empatía.

Estos cinco principios son consistentes con recomendaciones de diseño de instrucciones que buscan mejorar consistencia y utilidad del resultado (OpenAI, n.d.).


## Cierre argumentativo

La propuesta desarrollada para EcoMarket no plantea una sustitución total del trabajo humano, sino una automatización responsable de consultas repetitivas mediante una arquitectura híbrida. Su principal valor no está solo en usar un modelo generativo, sino en demostrar que la utilidad real surge cuando ese modelo se conecta con datos verificados, reglas de negocio, instrucciones bien diseñadas y criterios explícitos de supervisión. En ese sentido, el código no solo responde a la actividad; también representa una forma prudente y técnicamente defendible de pensar la IA generativa en contextos empresariales.

## Referencias

Autio, C., Schwartz, R., Dunietz, J., Jain, S., Stanley, M., Tabassi, E., Hall, P., & Roberts, K. (2024). *Artificial intelligence risk management framework: Generative artificial intelligence profile* (NIST AI 600-1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.AI.600-1

Gmyrek, P., Berg, J., Kamiński, K., Konopczyński, F., Ładna, A., Nafradi, B., Rosłaniec, K., & Troszyński, M. (2025). *Generative AI and jobs: A refined global index of occupational exposure* (ILO Working Paper 140). International Labour Organization. https://doi.org/10.54394/HETP0387

Hugging Face. (n.d.-a). *Transformers documentation*. https://huggingface.co/docs/transformers/index

OpenAI. (n.d.). *Prompt engineering*. OpenAI API Documentation. https://developers.openai.com/api/docs/guides/prompt-engineering

Organisation for Economic Co-operation and Development. (2024). *Using AI in the workplace: Opportunities, risks and policy responses* (OECD Artificial Intelligence Papers, No. 11). OECD Publishing. https://doi.org/10.1787/73d417f9-en

Organisation for Economic Co-operation and Development. (n.d.). *AI principles*. https://www.oecd.org/en/topics/ai-principles.html

Qwen. (n.d.). *Qwen2.5-0.5B-Instruct* [Model card]. Hugging Face. https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*. https://papers.nips.cc/paper/7181-attention-is-all-you-need
