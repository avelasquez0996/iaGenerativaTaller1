# Manual de uso del código  
## Taller Práctico #1 – EcoMarket

## 1. Propósito del programa

Este programa simula una solución de atención al cliente para la empresa ficticia **EcoMarket**, enfocada en dos tareas principales:

1. Consultar el **estado de pedidos**.
2. Orientar al cliente en el **proceso de devolución de productos**.

El sistema combina tres elementos:

- una base de datos simulada de pedidos,
- un conjunto de políticas de devolución,
- un modelo de lenguaje open-source para generar respuestas en lenguaje natural.

Además, el programa incluye un **modo de respaldo**, de forma que, si el modelo de IA no puede cargarse, el sistema sigue funcionando con respuestas estructuradas construidas directamente desde los datos.

## 2. Objetivo académico del código

Este código fue diseñado para apoyar la **fase práctica** del taller. En particular, permite demostrar cómo la **ingeniería de prompts** mejora la calidad de la respuesta del sistema. Para ello, el programa compara:

- un **prompt básico**, corto y poco específico;
- un **prompt mejorado**, con rol, contexto, restricciones y formato de salida.

De esta manera, el proyecto no solo responde al caso de estudio, sino que también evidencia la relación entre:

- datos estructurados,
- lógica de negocio,
- instrucciones al modelo,
- calidad de la respuesta final.

## 3. Requisitos del sistema

Antes de ejecutar el programa, es recomendable contar con:

- **Python 3.10 o superior**
- conexión a internet, en caso de que el modelo de Hugging Face deba descargarse por primera vez
- espacio suficiente para instalar dependencias y, eventualmente, almacenar el modelo en caché

### Dependencias principales

El programa utiliza las siguientes bibliotecas:

```bash
pip install torch transformers
```

Si deseas registrar las dependencias en un archivo, puedes crear un `requirements.txt` con este contenido:

```txt
torch
transformers
```

Luego puedes instalarlo con:

```bash
pip install -r requirements.txt
```

## 4. Estructura sugerida del proyecto

Se recomienda organizar el repositorio de la siguiente manera:

```text
entrega_taller_ecomarket/
├── main.py
├── requirements.txt
├── README.md
└── docs/
    ├── fase_1_modelo.md
    ├── fase_2_analisis.md
    └── manual_uso_codigo.md
```

Cuando el programa ejecuta la opción de generación de archivos, crea además esta estructura:

```text
entrega_taller_ecomarket/
├── README.md
├── datos/
│   ├── pedidos.json
│   ├── politicas_devolucion.json
│   └── catalogo_productos.json
└── docs/
    ├── fase_1_modelo.md
    └── fase_2_analisis.md
```

## 5. Cómo ejecutar el programa

Ubícate en la carpeta donde está guardado `main.py` y ejecuta:

```bash
python main.py
```

Al iniciar, el programa intenta cargar el modelo:

- si `torch` y `transformers` están disponibles y el modelo puede descargarse o cargarse correctamente, el sistema usará IA generativa;
- si ocurre un error, el programa activa el **modo de respaldo** y sigue funcionando con respuestas estructuradas.

## 6. Comportamiento inicial del sistema

Cuando el programa arranca, realiza estas acciones automáticamente:

1. Carga la base de pedidos con `cargar_base_pedidos()`.
2. Carga las políticas de devolución con `cargar_politicas_devolucion()`.
3. Carga el catálogo de productos con `cargar_catalogo_productos()`.
4. Crea índices para buscar más rápido pedidos y productos.
5. Intenta cargar el modelo `Qwen/Qwen2.5-0.5B-Instruct`.

Si todo funciona correctamente, aparecerá un mensaje similar a este:

```text
Cargando modelo open-source: Qwen/Qwen2.5-0.5B-Instruct
Dispositivo detectado: cpu
Modelo cargado correctamente.
```

Si no se puede cargar el modelo, aparecerá un aviso, pero el programa seguirá funcionando:

```text
[AVISO] No fue posible cargar el modelo: ...
Se activará el modo de respaldo para que el programa siga funcionando.
```

## 7. Menú principal

Una vez iniciado, el sistema muestra este menú:

```text
ECO MARKET - TALLER PRÁCTICO #1
1. Generar archivos Markdown y datos de la entrega
2. Comparar prompt básico vs mejorado para estado de pedido
3. Comparar prompt básico vs mejorado para devolución
4. Consultar estado de pedido
5. Consultar devolución de producto
0. Salir
```

Cada opción cumple una función específica.

## 8. Descripción de cada opción del menú

### Opción 1. Generar archivos Markdown y datos de la entrega

Esta opción crea automáticamente una carpeta llamada `entrega_taller_ecomarket` con:

- un archivo `README.md`,
- una carpeta `datos/` con archivos JSON,
- una carpeta `docs/` con los archivos Markdown de las fases 1 y 2.

#### Archivos generados

**En `datos/`:**
- `pedidos.json`
- `politicas_devolucion.json`
- `catalogo_productos.json`

**En `docs/`:**
- `fase_1_modelo.md`
- `fase_2_analisis.md`

**En la carpeta base:**
- `README.md`

#### Uso recomendado

Esta opción es útil cuando se desea preparar rápidamente la estructura del repositorio que será entregado en GitHub.

#### Resultado esperado

El programa mostrará este mensaje:

```text
Archivos generados correctamente en la carpeta 'entrega_taller_ecomarket'.
```

### Opción 2. Comparar prompt básico vs mejorado para estado de pedido

Esta opción permite demostrar, de manera práctica, cómo cambia la calidad de la respuesta cuando el prompt está mejor diseñado.

#### Qué solicita el sistema

El programa pedirá un número de seguimiento, por ejemplo:

```text
Ingresa el número de seguimiento (ejemplo: EM-1004):
```

#### Qué hace internamente

1. Genera un documento textual con todos los pedidos.
2. Busca el pedido específico ingresado.
3. Construye dos prompts:
   - uno básico,
   - uno mejorado.
4. Muestra ambos prompts.
5. Genera una respuesta para cada uno.

#### Diferencia entre ambos prompts

El **prompt básico** solo pide el estado del pedido usando la información disponible.

El **prompt mejorado** añade:
- un rol explícito para el modelo,
- reglas obligatorias,
- contexto verificado,
- instrucciones para no inventar datos,
- manejo de casos de retraso,
- estructura esperada de la respuesta.

#### Uso académico

Esta opción es especialmente importante para evidenciar la **ingeniería de prompts** en la fase 3 del taller.

### Opción 3. Comparar prompt básico vs mejorado para devolución

Esta opción cumple la misma lógica de comparación, pero aplicada al proceso de devoluciones.

#### Qué solicita el sistema

El programa pedirá:

- nombre del producto,
- categoría del producto, si no logra detectarla automáticamente,
- días desde la entrega,
- si conserva el empaque original,
- si presenta defecto.

#### Qué hace internamente

1. Genera el documento de políticas de devolución.
2. Evalúa el caso con la función `evaluar_devolucion(...)`.
3. Construye un prompt básico.
4. Construye un prompt mejorado.
5. Genera y muestra ambas respuestas.

#### Importancia de esta opción

Permite demostrar que no basta con preguntarle al modelo si “se puede devolver” un producto. La calidad de la respuesta mejora cuando se incluyen:

- contexto,
- restricciones,
- datos del caso,
- evaluación previa,
- tono empático.

### Opción 4. Consultar estado de pedido

Esta opción permite hacer una consulta directa, sin comparación entre prompts.

#### Flujo de uso

1. El usuario ingresa el número de seguimiento.
2. El sistema busca el pedido en la base.
3. Se genera un prompt mejorado.
4. El modelo produce una respuesta o, si no está disponible, se usa la respuesta de respaldo.

#### Ejemplo de entrada

```text
Ingresa el número de seguimiento: EM-1004
```

#### Posibles resultados

**Si el pedido existe:**
- se informa el estado actual,
- la fecha estimada de entrega,
- el enlace de rastreo,
- y, si aplica, una disculpa y motivo del retraso.

**Si el pedido no existe:**
- se informa amablemente que no fue encontrado,
- se sugiere verificar el número,
- y se menciona la posibilidad de acudir a un agente humano.

### Opción 5. Consultar devolución de producto

Esta opción permite analizar un caso de devolución de forma directa.

#### Flujo de uso

1. El usuario ingresa el nombre del producto.
2. El sistema intenta identificar su categoría usando el catálogo.
3. Si no la encuentra, pide la categoría manualmente.
4. Solicita:
   - días desde la entrega,
   - si conserva el empaque,
   - si el producto tiene defecto.
5. Evalúa el caso con las reglas de negocio.
6. Construye un prompt mejorado.
7. Genera una respuesta final.

#### Qué tipo de decisiones puede tomar el sistema

La devolución puede resultar:

- aprobada,
- no permitida por política,
- fuera de plazo,
- rechazada por falta de empaque original,
- o derivada a revisión si la categoría no se identifica.

#### Valor práctico

Esta opción demuestra que el modelo no toma la decisión por sí solo, sino que se apoya en una **evaluación previa basada en reglas**.

### Opción 0. Salir

Finaliza la ejecución del programa.

```text
Programa finalizado.
```

## 9. Explicación funcional del código

## 9.1. Carga de datos

### `cargar_base_pedidos()`

Devuelve una lista de diccionarios con 12 pedidos de ejemplo. Cada pedido incluye:

- número de seguimiento,
- cliente,
- producto,
- estado actual,
- fecha de compra,
- fecha estimada de entrega,
- transportadora,
- enlace de rastreo,
- indicador de retraso,
- motivo del retraso.

Esta función cumple un papel central, porque proporciona la base para la consulta de pedidos.

### `cargar_politicas_devolucion()`

Devuelve un diccionario cuyas claves son categorías de producto y cuyos valores son políticas de devolución. Cada política contiene:

- si admite devolución,
- días máximos,
- si requiere empaque original,
- si acepta cambio por defecto,
- motivo de restricción.

Gracias a esta función, el sistema puede tomar decisiones consistentes frente a solicitudes de devolución.

### `cargar_catalogo_productos()`

Devuelve una lista de productos y su categoría correspondiente. Esto permite detectar automáticamente la categoría del producto cuando el usuario la escribe correctamente.

## 9.2. Creación de índices

### `crear_indice_pedidos(base_pedidos)`

Convierte la lista de pedidos en un diccionario cuya clave es el número de seguimiento. Esto acelera la búsqueda.

### `crear_indice_productos(catalogo_productos)`

Convierte la lista de productos en un diccionario cuya clave es el nombre del producto en minúsculas. También mejora la velocidad de consulta.

## 9.3. Generación de documentos de contexto

### `generar_documento_pedidos(base_pedidos)`

Construye un texto con todos los pedidos en un formato legible. Este documento se incluye en el prompt para que el modelo responda con base en información explícita.

### `generar_documento_politicas(politicas_devolucion)`

Construye un texto con todas las políticas de devolución. Se usa como contexto para orientar la respuesta del modelo.

## 9.4. Funciones de búsqueda

### `buscar_pedido(numero_seguimiento, indice_pedidos)`

Busca un pedido por número de seguimiento, normalizando la entrada a mayúsculas.

### `buscar_producto(nombre_producto, indice_productos)`

Busca un producto por nombre, normalizando el texto a minúsculas.

## 9.5. Lógica de negocio para devoluciones

### `evaluar_devolucion(...)`

Esta es una de las funciones más importantes del programa. No genera lenguaje, sino que **toma una decisión estructurada** sobre la posibilidad de devolver un producto.

Evalúa, en orden:

1. si la categoría existe,
2. si el producto está defectuoso y admite cambio,
3. si la categoría permite devolución,
4. si la solicitud está dentro del plazo,
5. si el producto conserva el empaque original.

Devuelve un diccionario con:

- `aprobada`
- `tipo_solucion`
- `motivo`
- `pasos`

Esto permite separar la **decisión lógica** de la **redacción de la respuesta**.

## 9.6. Construcción de prompts

### `construir_prompt_basico_pedido(...)`

Genera un prompt corto para consultar el estado del pedido.

### `construir_prompt_mejorado_pedido(...)`

Genera un prompt detallado con:
- rol,
- reglas,
- contexto,
- registro específico,
- formato sugerido.

### `construir_prompt_basico_devolucion(...)`

Genera una pregunta básica para saber si un producto puede devolverse.

### `construir_prompt_mejorado_devolucion(...)`

Genera un prompt más robusto con:
- tono empático,
- reglas obligatorias,
- datos del caso,
- políticas,
- evaluación previa,
- formato sugerido.

## 9.7. Motor generativo

### Clase `MotorGenerativoEcoMarket`

Esta clase encapsula toda la interacción con el modelo de lenguaje.

#### Método `__init__`

Inicializa:
- nombre del modelo,
- modelo,
- tokenizador,
- dispositivo,
- indicador de modo de respaldo.

#### Método `cargar_modelo()`

Intenta cargar el modelo desde Hugging Face. También detecta si hay GPU disponible.

Si ocurre un problema:
- activa el modo de respaldo,
- evita que el programa se detenga.

#### Método `generar_respuesta(prompt, temperatura, max_nuevos_tokens)`

Recibe un prompt y genera una respuesta.

Si el modelo no está disponible:
- retorna un aviso de respaldo.

Si el modelo funciona:
- construye la entrada,
- tokeniza,
- genera la salida,
- la decodifica y la devuelve como texto.

## 9.8. Respuestas de respaldo

### `construir_respuesta_respaldo_pedido(...)`

Genera una respuesta predeterminada a partir de los datos del pedido, sin usar IA generativa.

### `construir_respuesta_respaldo_devolucion(...)`

Hace lo mismo para los casos de devolución.

Estas funciones son esenciales porque garantizan continuidad del servicio.

## 9.9. Función de generación de archivos

### `generar_archivos_markdown_y_datos()`

Crea la estructura de carpetas y archivos para la entrega del taller. Es útil para organizar la documentación y los datos del proyecto.

## 9.10. Funciones de interacción con el usuario

### `leer_booleano(mensaje)`

Permite capturar respuestas afirmativas o negativas del usuario y convertirlas a valores booleanos.

### `mostrar_menu()`

Imprime el menú principal.

### `ejecutar_aplicacion()`

Es la función principal del sistema. Controla el flujo completo del programa:
- carga datos,
- inicializa el motor,
- muestra el menú,
- ejecuta la opción elegida por el usuario.

## 10. Ejemplos de uso

## 10.1. Consulta de pedido

### Entrada del usuario

```text
Selecciona una opción: 4
Ingresa el número de seguimiento: EM-1011
```

### Resultado esperado

El sistema responderá con información como:
- estado actual,
- fecha estimada,
- enlace de rastreo,
- motivo del retraso, si existe.

## 10.2. Consulta de devolución

### Entrada del usuario

```text
Selecciona una opción: 5
Nombre del producto: Shampoo sólido natural
Días desde la entrega: 5
¿Conserva empaque original? (si/no): si
¿El producto presenta defecto? (si/no): no
```

### Resultado esperado

El sistema analizará la categoría `cuidado_personal` y responderá que la devolución estándar no es posible por razones sanitarias, usando un tono empático.

## 10.3. Caso de producto defectuoso

### Entrada del usuario

```text
Selecciona una opción: 5
Nombre del producto: Cepillo dental de bambú
Días desde la entrega: 3
¿Conserva empaque original? (si/no): si
¿El producto presenta defecto? (si/no): si
```

### Resultado esperado

El sistema podrá sugerir cambio o revisión por defecto, siempre que la política de la categoría lo permita.

## 11. Solución de problemas frecuentes

## El modelo no carga

### Posibles causas
- `torch` no está instalado.
- `transformers` no está instalado.
- no hay conexión a internet para descargar el modelo.
- falta memoria RAM o espacio en disco.

### Solución
Instala las dependencias:

```bash
pip install torch transformers
```

Si el problema persiste, el programa seguirá funcionando en **modo de respaldo**.

## El producto no se encuentra en el catálogo

Si el nombre ingresado no coincide exactamente con uno del catálogo, el sistema pedirá la categoría manualmente. Esto no es un error: es un mecanismo previsto para mantener la consulta funcionando.

## El pedido no existe

Si el número ingresado no está en la base, el sistema responderá que no fue encontrado y sugerirá verificarlo.

## Los archivos Markdown no aparecen

Asegúrate de haber ejecutado la **opción 1** del menú. Esa es la que crea la carpeta `entrega_taller_ecomarket`.
