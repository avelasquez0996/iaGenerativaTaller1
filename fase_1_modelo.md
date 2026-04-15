# Fase 1 - Selección y justificación del modelo de IA

## Modelo propuesto
Se propone una **solución híbrida** compuesta por:

1. Un **modelo de lenguaje open-source instruct** para redactar respuestas naturales.
2. Un sistema de **recuperación de información** conectado a la base de datos de EcoMarket.
3. Un módulo de **reglas de negocio** para validar devoluciones, estados de pedidos y restricciones.
4. Un mecanismo de **escalamiento a agente humano** para los casos complejos.

## ¿Por qué este enfoque?
EcoMarket tiene dos tipos de solicitudes:
- El 80% son repetitivas y estructuradas.
- El 20% son complejas y requieren empatía, criterio o manejo delicado.

Un LLM por sí solo puede redactar bien, pero puede alucinar.  
Un sistema rígido basado solo en reglas sería preciso, pero poco natural.

Por eso, la mejor alternativa es una arquitectura híbrida:
- **Precisión** para pedidos, devoluciones y políticas mediante recuperación y reglas.
- **Fluidez** en el lenguaje mediante un modelo generativo.
- **Escalabilidad** al automatizar gran parte de las consultas frecuentes.
- **Seguridad** al limitar la invención de datos.

## Arquitectura propuesta
1. El cliente envía una consulta por chat, correo o red social.
2. El sistema clasifica la intención:
   - Estado del pedido
   - Devolución
   - Información del producto
   - Caso complejo
3. Si es una consulta repetitiva:
   - Se consulta la base de datos o el catálogo
   - Se construye un prompt con contexto verificado
   - El modelo genera una respuesta amable
4. Si es un caso complejo:
   - Se deriva a un agente humano
   - El sistema puede generar un borrador de respuesta
5. Se registra la interacción para auditoría y mejora continua.

## Justificación por criterios

### Costo
Un modelo open-source reduce dependencia de proveedores cerrados y permite pruebas locales o en servidores propios.

### Escalabilidad
La automatización del 80% de las consultas repetitivas reduce la carga del equipo humano y mejora tiempos de respuesta.

### Facilidad de integración
El modelo puede conectarse con:
- Base de datos de pedidos
- Catálogo de productos
- Políticas de devolución
- CRM o sistema de tickets

### Calidad esperada de la respuesta
La calidad mejora cuando el modelo recibe:
- un rol claro,
- contexto verificado,
- reglas de negocio,
- formato deseado de salida.

## Conclusión de diseño
La mejor propuesta para EcoMarket no es reemplazar completamente al equipo humano, sino **combinar IA generativa con recuperación de datos y supervisión humana**.