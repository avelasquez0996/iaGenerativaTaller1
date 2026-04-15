# Fase 2 - Fortalezas, limitaciones y riesgos éticos

## Fortalezas
- Atención 24/7.
- Reducción del tiempo promedio de respuesta.
- Capacidad para resolver gran parte de las consultas repetitivas.
- Respuestas más consistentes.
- Menor carga operativa para el equipo humano.
- Mejor experiencia para el cliente en consultas simples.

## Limitaciones
- No reemplaza bien la empatía humana en quejas complejas.
- Puede fallar si la base de datos está desactualizada.
- Depende de una buena clasificación de intenciones.
- Puede interpretar mal mensajes ambiguos.
- Requiere monitoreo permanente y mejora continua.

## Riesgos éticos

### 1. Alucinaciones
El modelo podría inventar información sobre estados de pedidos, reembolsos o políticas.

**Mitigación:**
- usar contexto verificado,
- prohibir respuestas sin evidencia en el prompt,
- validar campos críticos con reglas de negocio.

### 2. Sesgos
El modelo podría responder mejor a ciertos estilos de escritura, regiones o perfiles de clientes.

**Mitigación:**
- evaluar respuestas con diversidad de usuarios,
- revisar resultados periódicamente,
- incluir supervisión humana en casos sensibles.

### 3. Privacidad de datos
El sistema manejará direcciones, nombres, historial de compras y números de pedido.

**Mitigación:**
- minimización de datos en los prompts,
- control de acceso,
- cifrado,
- anonimización cuando sea posible,
- cumplimiento de políticas de protección de datos.

### 4. Impacto laboral
Existe el riesgo de que la IA se perciba como un reemplazo del personal de soporte.

**Mitigación:**
- redefinir el rol del agente como supervisor y resolvedor de casos complejos,
- usar la IA como herramienta de apoyo,
- capacitar al personal para trabajar con sistemas de IA.

## Postura recomendada
La implementación debe orientarse a **empoderar** a los agentes humanos, no a eliminarlos.