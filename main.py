import json
import textwrap
from pathlib import Path
from typing import Dict, List, Optional

try:
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    TRANSFORMERS_DISPONIBLE = True
except Exception:
    TRANSFORMERS_DISPONIBLE = False


def cargar_base_pedidos() -> List[Dict]:
    return [
        {
            "numero_seguimiento": "EM-1001",
            "cliente": "Laura Gómez",
            "producto": "Botella térmica de acero reciclado",
            "estado_actual": "Entregado",
            "fecha_compra": "2026-04-01",
            "fecha_estimada_entrega": "2026-04-05",
            "transportadora": "EcoEnvíos",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1001",
            "retrasado": False,
            "motivo_retraso": ""
        },
        {
            "numero_seguimiento": "EM-1002",
            "cliente": "Carlos Pérez",
            "producto": "Cepillo dental de bambú",
            "estado_actual": "En tránsito",
            "fecha_compra": "2026-04-10",
            "fecha_estimada_entrega": "2026-04-16",
            "transportadora": "RutaVerde",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1002",
            "retrasado": False,
            "motivo_retraso": ""
        },
        {
            "numero_seguimiento": "EM-1003",
            "cliente": "Mariana Rojas",
            "producto": "Kit de cubiertos reutilizables",
            "estado_actual": "Procesando en bodega",
            "fecha_compra": "2026-04-14",
            "fecha_estimada_entrega": "2026-04-19",
            "transportadora": "BioLogística",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1003",
            "retrasado": False,
            "motivo_retraso": ""
        },
        {
            "numero_seguimiento": "EM-1004",
            "cliente": "Sofía Torres",
            "producto": "Shampoo sólido natural",
            "estado_actual": "Retrasado en centro logístico",
            "fecha_compra": "2026-04-07",
            "fecha_estimada_entrega": "2026-04-12",
            "transportadora": "EcoEnvíos",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1004",
            "retrasado": True,
            "motivo_retraso": "Alta demanda por temporada y congestión en el centro de distribución."
        },
        {
            "numero_seguimiento": "EM-1005",
            "cliente": "Andrés Ruiz",
            "producto": "Toallas de algodón orgánico",
            "estado_actual": "Listo para despacho",
            "fecha_compra": "2026-04-13",
            "fecha_estimada_entrega": "2026-04-18",
            "transportadora": "RutaVerde",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1005",
            "retrasado": False,
            "motivo_retraso": ""
        },
        {
            "numero_seguimiento": "EM-1006",
            "cliente": "Valentina Díaz",
            "producto": "Bolsa compostable para residuos",
            "estado_actual": "Entregado",
            "fecha_compra": "2026-03-28",
            "fecha_estimada_entrega": "2026-04-02",
            "transportadora": "BioLogística",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1006",
            "retrasado": False,
            "motivo_retraso": ""
        },
        {
            "numero_seguimiento": "EM-1007",
            "cliente": "Nicolás Mejía",
            "producto": "Detergente ecológico concentrado",
            "estado_actual": "En tránsito",
            "fecha_compra": "2026-04-11",
            "fecha_estimada_entrega": "2026-04-17",
            "transportadora": "EcoEnvíos",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1007",
            "retrasado": False,
            "motivo_retraso": ""
        },
        {
            "numero_seguimiento": "EM-1008",
            "cliente": "Paula Herrera",
            "producto": "Esponja vegetal biodegradable",
            "estado_actual": "Pendiente de pago confirmado",
            "fecha_compra": "2026-04-15",
            "fecha_estimada_entrega": "2026-04-20",
            "transportadora": "RutaVerde",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1008",
            "retrasado": False,
            "motivo_retraso": ""
        },
        {
            "numero_seguimiento": "EM-1009",
            "cliente": "Julián Castro",
            "producto": "Vela aromática de cera vegetal",
            "estado_actual": "Entregado",
            "fecha_compra": "2026-04-03",
            "fecha_estimada_entrega": "2026-04-08",
            "transportadora": "BioLogística",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1009",
            "retrasado": False,
            "motivo_retraso": ""
        },
        {
            "numero_seguimiento": "EM-1010",
            "cliente": "Diana Mora",
            "producto": "Pañuelos reutilizables de tela",
            "estado_actual": "En reparto",
            "fecha_compra": "2026-04-09",
            "fecha_estimada_entrega": "2026-04-15",
            "transportadora": "EcoEnvíos",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1010",
            "retrasado": False,
            "motivo_retraso": ""
        },
        {
            "numero_seguimiento": "EM-1011",
            "cliente": "Camilo Vega",
            "producto": "Kit de higiene personal ecológico",
            "estado_actual": "Retrasado en aduana local",
            "fecha_compra": "2026-04-05",
            "fecha_estimada_entrega": "2026-04-11",
            "transportadora": "RutaVerde",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1011",
            "retrasado": True,
            "motivo_retraso": "Inspección extraordinaria de paquetería en aduana local."
        },
        {
            "numero_seguimiento": "EM-1012",
            "cliente": "Sara Londoño",
            "producto": "Snacks orgánicos de frutas deshidratadas",
            "estado_actual": "Entregado",
            "fecha_compra": "2026-04-02",
            "fecha_estimada_entrega": "2026-04-06",
            "transportadora": "BioLogística",
            "enlace_rastreo": "https://ecomarket.com/rastreo/EM-1012",
            "retrasado": False,
            "motivo_retraso": ""
        }
    ]


def cargar_politicas_devolucion() -> Dict[str, Dict]:
    return {
        "accesorios": {
            "admite_devolucion": True,
            "dias_maximos": 30,
            "requiere_empaque_original": True,
            "acepta_cambio_si_defectuoso": True,
            "motivo_no_devolucion": ""
        },
        "cuidado_personal": {
            "admite_devolucion": False,
            "dias_maximos": 0,
            "requiere_empaque_original": True,
            "acepta_cambio_si_defectuoso": True,
            "motivo_no_devolucion": "Los productos de higiene o cuidado personal no pueden devolverse por seguridad sanitaria."
        },
        "textiles": {
            "admite_devolucion": True,
            "dias_maximos": 30,
            "requiere_empaque_original": False,
            "acepta_cambio_si_defectuoso": True,
            "motivo_no_devolucion": ""
        },
        "limpieza": {
            "admite_devolucion": True,
            "dias_maximos": 15,
            "requiere_empaque_original": True,
            "acepta_cambio_si_defectuoso": True,
            "motivo_no_devolucion": ""
        },
        "alimentos": {
            "admite_devolucion": False,
            "dias_maximos": 0,
            "requiere_empaque_original": True,
            "acepta_cambio_si_defectuoso": False,
            "motivo_no_devolucion": "Los productos perecederos o de consumo alimentario no admiten devolución."
        },
        "hogar": {
            "admite_devolucion": True,
            "dias_maximos": 20,
            "requiere_empaque_original": True,
            "acepta_cambio_si_defectuoso": True,
            "motivo_no_devolucion": ""
        }
    }


def cargar_catalogo_productos() -> List[Dict]:
    return [
        {"nombre": "Botella térmica de acero reciclado", "categoria": "accesorios"},
        {"nombre": "Cepillo dental de bambú", "categoria": "cuidado_personal"},
        {"nombre": "Kit de cubiertos reutilizables", "categoria": "accesorios"},
        {"nombre": "Shampoo sólido natural", "categoria": "cuidado_personal"},
        {"nombre": "Toallas de algodón orgánico", "categoria": "textiles"},
        {"nombre": "Bolsa compostable para residuos", "categoria": "hogar"},
        {"nombre": "Detergente ecológico concentrado", "categoria": "limpieza"},
        {"nombre": "Esponja vegetal biodegradable", "categoria": "hogar"},
        {"nombre": "Vela aromática de cera vegetal", "categoria": "hogar"},
        {"nombre": "Pañuelos reutilizables de tela", "categoria": "textiles"},
        {"nombre": "Kit de higiene personal ecológico", "categoria": "cuidado_personal"},
        {"nombre": "Snacks orgánicos de frutas deshidratadas", "categoria": "alimentos"}
    ]


def crear_indice_pedidos(base_pedidos: List[Dict]) -> Dict[str, Dict]:
    return {pedido["numero_seguimiento"]: pedido for pedido in base_pedidos}


def crear_indice_productos(catalogo_productos: List[Dict]) -> Dict[str, Dict]:
    return {producto["nombre"].lower(): producto for producto in catalogo_productos}


def generar_documento_pedidos(base_pedidos: List[Dict]) -> str:
    lineas = ["DOCUMENTO DE PEDIDOS DE ECOMARKET"]
    for pedido in base_pedidos:
        lineas.append(
            (
                f"- Número: {pedido['numero_seguimiento']} | Cliente: {pedido['cliente']} | "
                f"Producto: {pedido['producto']} | Estado: {pedido['estado_actual']} | "
                f"Fecha de compra: {pedido['fecha_compra']} | "
                f"Fecha estimada de entrega: {pedido['fecha_estimada_entrega']} | "
                f"Transportadora: {pedido['transportadora']} | "
                f"Enlace de rastreo: {pedido['enlace_rastreo']} | "
                f"Retrasado: {'Sí' if pedido['retrasado'] else 'No'} | "
                f"Motivo del retraso: {pedido['motivo_retraso'] or 'No aplica'}"
            )
        )
    return "\n".join(lineas)


def generar_documento_politicas(politicas_devolucion: Dict[str, Dict]) -> str:
    lineas = ["DOCUMENTO DE POLÍTICAS DE DEVOLUCIÓN DE ECOMARKET"]
    for categoria, politica in politicas_devolucion.items():
        lineas.append(
            (
                f"- Categoría: {categoria} | Admite devolución: {'Sí' if politica['admite_devolucion'] else 'No'} | "
                f"Días máximos: {politica['dias_maximos']} | "
                f"Requiere empaque original: {'Sí' if politica['requiere_empaque_original'] else 'No'} | "
                f"Acepta cambio si está defectuoso: {'Sí' if politica['acepta_cambio_si_defectuoso'] else 'No'} | "
                f"Motivo de restricción: {politica['motivo_no_devolucion'] or 'No aplica'}"
            )
        )
    return "\n".join(lineas)


def buscar_pedido(numero_seguimiento: str, indice_pedidos: Dict[str, Dict]) -> Optional[Dict]:
    return indice_pedidos.get(numero_seguimiento.strip().upper())


def buscar_producto(nombre_producto: str, indice_productos: Dict[str, Dict]) -> Optional[Dict]:
    return indice_productos.get(nombre_producto.strip().lower())


def evaluar_devolucion(
    nombre_producto: str,
    categoria_producto: str,
    dias_desde_entrega: int,
    con_empaque_original: bool,
    producto_defectuoso: bool,
    politicas_devolucion: Dict[str, Dict]
) -> Dict:
    categoria_normalizada = categoria_producto.strip().lower()

    if categoria_normalizada not in politicas_devolucion:
        return {
            "aprobada": False,
            "tipo_solucion": "sin categoría identificada",
            "motivo": (
                f"No fue posible identificar una política de devolución para la categoría "
                f"'{categoria_producto}'. Se requiere revisión por un agente humano."
            ),
            "pasos": [
                "Verificar la categoría real del producto en el catálogo.",
                "Escalar el caso a un agente humano."
            ]
        }

    politica = politicas_devolucion[categoria_normalizada]

    if producto_defectuoso and politica["acepta_cambio_si_defectuoso"]:
        return {
            "aprobada": True,
            "tipo_solucion": "cambio o revisión por defecto",
            "motivo": (
                f"El producto '{nombre_producto}' reporta defecto y la política de la categoría "
                f"'{categoria_normalizada}' permite gestionar cambio o revisión."
            ),
            "pasos": [
                "Solicitar fotos o evidencia del defecto.",
                "Validar el número de pedido.",
                "Generar guía de devolución o cambio.",
                "Informar el tiempo estimado de resolución."
            ]
        }

    if not politica["admite_devolucion"]:
        return {
            "aprobada": False,
            "tipo_solucion": "devolución no permitida",
            "motivo": politica["motivo_no_devolucion"],
            "pasos": [
                "Explicar con empatía la restricción de la categoría.",
                "Ofrecer revisión manual solo si existe error de despacho.",
                "Derivar a un agente si el cliente insiste o reporta una excepción."
            ]
        }

    if dias_desde_entrega > politica["dias_maximos"]:
        return {
            "aprobada": False,
            "tipo_solucion": "fuera de plazo",
            "motivo": (
                f"La solicitud supera el plazo máximo de {politica['dias_maximos']} días "
                f"para la categoría '{categoria_normalizada}'."
            ),
            "pasos": [
                "Informar al cliente que el plazo de devolución expiró.",
                "Ofrecer revisión excepcional por parte de soporte si existe defecto no reportado."
            ]
        }

    if politica["requiere_empaque_original"] and not con_empaque_original:
        return {
            "aprobada": False,
            "tipo_solucion": "falta de empaque original",
            "motivo": (
                f"La categoría '{categoria_normalizada}' requiere empaque original para procesar la devolución."
            ),
            "pasos": [
                "Informar la condición de empaque original.",
                "Ofrecer revisión manual si hubo daño de fábrica."
            ]
        }

    return {
        "aprobada": True,
        "tipo_solucion": "devolución aprobada",
        "motivo": (
            f"La devolución del producto '{nombre_producto}' cumple la política de la categoría "
            f"'{categoria_normalizada}'."
        ),
        "pasos": [
            "Confirmar número de pedido y datos del cliente.",
            "Enviar guía de devolución.",
            "Indicar plazo de inspección del producto.",
            "Notificar el tiempo estimado del reembolso o cambio."
        ]
    }


def construir_prompt_basico_pedido(numero_seguimiento: str, documento_pedidos: str) -> str:
    return textwrap.dedent(
        f"""
        Dame el estado del pedido {numero_seguimiento} usando esta información:

        {documento_pedidos}
        """
    ).strip()


def construir_prompt_mejorado_pedido(
    numero_seguimiento: str,
    documento_pedidos: str,
    pedido_encontrado: Optional[Dict]
) -> str:
    registro_relevante = (
        json.dumps(pedido_encontrado, ensure_ascii=False, indent=2)
        if pedido_encontrado
        else "No se encontró un registro exacto para ese número de seguimiento."
    )

    return textwrap.dedent(
        f"""
        Actúa como un agente de servicio al cliente amable, claro y profesional de EcoMarket.

        Tu tarea es responder una consulta sobre el estado de un pedido.

        Reglas obligatorias:
        1. Usa exclusivamente la información del documento de pedidos y del registro identificado.
        2. No inventes datos que no aparezcan en el contexto.
        3. Si no existe el pedido, indícalo con amabilidad y sugiere verificar el número de seguimiento.
        4. Si el pedido está retrasado, ofrece una disculpa breve e incluye la razón del retraso.
        5. Si existe fecha estimada de entrega, inclúyela.
        6. Si existe enlace de rastreo, compártelo.
        7. Responde en español.
        8. Mantén un tono humano y útil.

        DOCUMENTO DE PEDIDOS:
        {documento_pedidos}

        REGISTRO IDENTIFICADO:
        {registro_relevante}

        NÚMERO CONSULTADO:
        {numero_seguimiento}

        Formato sugerido de respuesta:
        - Saludo breve
        - Estado actual del pedido
        - Fecha estimada de entrega
        - Enlace de rastreo
        - Mensaje adicional si hay retraso
        """
    ).strip()


def construir_prompt_basico_devolucion(
    nombre_producto: str,
    categoria_producto: str,
    documento_politicas: str
) -> str:
    return textwrap.dedent(
        f"""
        ¿Se puede devolver el producto '{nombre_producto}' de la categoría '{categoria_producto}'?
        Usa esta política:

        {documento_politicas}
        """
    ).strip()


def construir_prompt_mejorado_devolucion(
    nombre_producto: str,
    categoria_producto: str,
    dias_desde_entrega: int,
    con_empaque_original: bool,
    producto_defectuoso: bool,
    documento_politicas: str,
    evaluacion_previa: Dict
) -> str:
    return textwrap.dedent(
        f"""
        Actúa como un agente de servicio al cliente empático, claro y profesional de EcoMarket.

        Debes orientar al cliente sobre una devolución de producto.

        Reglas obligatorias:
        1. Usa solo la información del documento de políticas y de la evaluación previa.
        2. No inventes políticas.
        3. Si la devolución no es posible, explícalo con empatía y claridad.
        4. Si hay una alternativa como cambio por defecto o revisión manual, menciónala.
        5. Responde en español.
        6. Usa un tono cordial y fácil de entender.

        DATOS DEL CASO:
        - Producto: {nombre_producto}
        - Categoría: {categoria_producto}
        - Días desde la entrega: {dias_desde_entrega}
        - Tiene empaque original: {"Sí" if con_empaque_original else "No"}
        - Reporta defecto: {"Sí" if producto_defectuoso else "No"}

        DOCUMENTO DE POLÍTICAS:
        {documento_politicas}

        EVALUACIÓN PREVIA:
        {json.dumps(evaluacion_previa, ensure_ascii=False, indent=2)}

        Formato sugerido:
        - Saludo breve
        - Decisión principal
        - Explicación sencilla
        - Pasos siguientes
        """
    ).strip()


class MotorGenerativoEcoMarket:
    def __init__(self, nombre_modelo: str = "Qwen/Qwen2.5-0.5B-Instruct"):
        self.nombre_modelo = nombre_modelo
        self.modelo = None
        self.tokenizador = None
        self.dispositivo = "cpu"
        self.modo_respaldo = True

    def cargar_modelo(self) -> None:
        if not TRANSFORMERS_DISPONIBLE:
            print("\n[AVISO] transformers/torch no están disponibles. Se activará el modo de respaldo.\n")
            self.modo_respaldo = True
            return

        try:
            self.dispositivo = "cuda" if torch.cuda.is_available() else "cpu"
            print(f"\nCargando modelo open-source: {self.nombre_modelo}")
            print(f"Dispositivo detectado: {self.dispositivo}")

            self.tokenizador = AutoTokenizer.from_pretrained(self.nombre_modelo)

            tipo_dato = torch.float16 if self.dispositivo == "cuda" else torch.float32
            self.modelo = AutoModelForCausalLM.from_pretrained(
                self.nombre_modelo,
                torch_dtype=tipo_dato
            )
            self.modelo.to(self.dispositivo)
            self.modelo.eval()

            if self.tokenizador.pad_token is None:
                self.tokenizador.pad_token = self.tokenizador.eos_token

            self.modo_respaldo = False
            print("Modelo cargado correctamente.\n")

        except Exception as error:
            print(f"\n[AVISO] No fue posible cargar el modelo: {error}")
            print("Se activará el modo de respaldo para que el programa siga funcionando.\n")
            self.modo_respaldo = True

    def generar_respuesta(self, prompt: str, temperatura: float = 0.3, max_nuevos_tokens: int = 220) -> str:
        if self.modo_respaldo or self.modelo is None or self.tokenizador is None:
            return "[MODO RESPALDO] No se generó respuesta con el modelo. Usa la respuesta estructurada del sistema."

        try:
            if hasattr(self.tokenizador, "apply_chat_template"):
                mensajes = [
                    {
                        "role": "system",
                        "content": (
                            "Eres un asistente útil para servicio al cliente de EcoMarket. "
                            "Responde en español, con precisión y sin inventar información."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
                texto_entrada = self.tokenizador.apply_chat_template(
                    mensajes,
                    tokenize=False,
                    add_generation_prompt=True
                )
            else:
                texto_entrada = prompt

            entradas = self.tokenizador(
                texto_entrada,
                return_tensors="pt",
                truncation=True,
                max_length=2048
            ).to(self.dispositivo)

            with torch.no_grad():
                salidas = self.modelo.generate(
                    **entradas,
                    max_new_tokens=max_nuevos_tokens,
                    do_sample=True,
                    temperature=temperatura,
                    top_p=0.9,
                    repetition_penalty=1.1,
                    pad_token_id=self.tokenizador.eos_token_id
                )

            longitud_entrada = entradas["input_ids"].shape[1]
            tokens_generados = salidas[0][longitud_entrada:]
            respuesta = self.tokenizador.decode(tokens_generados, skip_special_tokens=True).strip()

            if not respuesta:
                return "[MODO RESPALDO] El modelo no produjo texto útil. Usa la respuesta estructurada del sistema."

            return respuesta

        except Exception as error:
            return f"[MODO RESPALDO] Error al generar con el modelo: {error}"


def construir_respuesta_respaldo_pedido(pedido: Optional[Dict], numero_seguimiento: str) -> str:
    if pedido is None:
        return (
            f"Hola. No encontré un pedido asociado al número de seguimiento {numero_seguimiento}. "
            f"Por favor revisa el número e inténtalo nuevamente. Si el problema continúa, "
            f"un agente humano puede ayudarte a verificar la compra."
        )

    respuesta = (
        f"Hola. El pedido {pedido['numero_seguimiento']} correspondiente a "
        f"'{pedido['producto']}' está actualmente en estado: {pedido['estado_actual']}. "
        f"La fecha estimada de entrega es {pedido['fecha_estimada_entrega']}. "
        f"Puedes consultar el rastreo aquí: {pedido['enlace_rastreo']}."
    )

    if pedido["retrasado"]:
        respuesta += (
            f" Lamentamos la demora. El retraso se debe a lo siguiente: {pedido['motivo_retraso']}"
        )

    return respuesta


def construir_respuesta_respaldo_devolucion(evaluacion_previa: Dict) -> str:
    if evaluacion_previa["aprobada"]:
        pasos = "; ".join(evaluacion_previa["pasos"])
        return (
            f"Hola. Sí es posible continuar con la solicitud. "
            f"Decisión: {evaluacion_previa['tipo_solucion']}. "
            f"Motivo: {evaluacion_previa['motivo']}. "
            f"Pasos siguientes: {pasos}."
        )

    pasos = "; ".join(evaluacion_previa["pasos"])
    return (
        f"Hola. Entiendo la situación y con gusto te orientaré. "
        f"En este caso, la solicitud no puede procesarse como devolución estándar. "
        f"Decisión: {evaluacion_previa['tipo_solucion']}. "
        f"Motivo: {evaluacion_previa['motivo']}. "
        f"Pasos sugeridos: {pasos}."
    )


def generar_archivos_markdown_y_datos() -> None:
    carpeta_base = Path("entrega_taller_ecomarket")
    carpeta_datos = carpeta_base / "datos"
    carpeta_docs = carpeta_base / "docs"

    carpeta_base.mkdir(exist_ok=True)
    carpeta_datos.mkdir(exist_ok=True)
    carpeta_docs.mkdir(exist_ok=True)

    base_pedidos = cargar_base_pedidos()
    politicas_devolucion = cargar_politicas_devolucion()
    catalogo_productos = cargar_catalogo_productos()

    with open(carpeta_datos / "pedidos.json", "w", encoding="utf-8") as archivo:
        json.dump(base_pedidos, archivo, ensure_ascii=False, indent=2)

    with open(carpeta_datos / "politicas_devolucion.json", "w", encoding="utf-8") as archivo:
        json.dump(politicas_devolucion, archivo, ensure_ascii=False, indent=2)

    with open(carpeta_datos / "catalogo_productos.json", "w", encoding="utf-8") as archivo:
        json.dump(catalogo_productos, archivo, ensure_ascii=False, indent=2)

    contenido_fase_1 = textwrap.dedent(
        """
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
        """
    ).strip()

    contenido_fase_2 = textwrap.dedent(
        """
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
        """
    ).strip()

    contenido_readme = textwrap.dedent(
        """
        # Taller Práctico #1 - EcoMarket

        Este repositorio contiene una propuesta de solución para optimizar la atención al cliente de EcoMarket.

        ## Estructura
        - `docs/fase_1_modelo.md`
        - `docs/fase_2_analisis.md`
        - `datos/pedidos.json`
        - `datos/politicas_devolucion.json`
        - `datos/catalogo_productos.json`
        - `main.py`

        ## Requisitos
        ```bash
        pip install torch transformers
        ```

        ## Ejecución
        ```bash
        python main.py
        ```

        ## Enfoque técnico
        Se usa una solución híbrida:
        - contexto estructurado,
        - reglas de negocio,
        - modelo open-source instruct,
        - escalamiento humano cuando sea necesario.
        """
    ).strip()

    with open(carpeta_docs / "fase_1_modelo.md", "w", encoding="utf-8") as archivo:
        archivo.write(contenido_fase_1)

    with open(carpeta_docs / "fase_2_analisis.md", "w", encoding="utf-8") as archivo:
        archivo.write(contenido_fase_2)

    with open(carpeta_base / "README.md", "w", encoding="utf-8") as archivo:
        archivo.write(contenido_readme)

    print("\nArchivos generados correctamente en la carpeta 'entrega_taller_ecomarket'.\n")


def imprimir_separador() -> None:
    print("\n" + "=" * 100 + "\n")


def comparar_prompts_pedido(
    motor: MotorGenerativoEcoMarket,
    numero_seguimiento: str,
    base_pedidos: List[Dict],
    indice_pedidos: Dict[str, Dict]
) -> None:
    documento_pedidos = generar_documento_pedidos(base_pedidos)
    pedido_encontrado = buscar_pedido(numero_seguimiento, indice_pedidos)

    prompt_basico = construir_prompt_basico_pedido(numero_seguimiento, documento_pedidos)
    prompt_mejorado = construir_prompt_mejorado_pedido(numero_seguimiento, documento_pedidos, pedido_encontrado)

    print("PROMPT BÁSICO:\n")
    print(prompt_basico)

    imprimir_separador()

    print("RESPUESTA AL PROMPT BÁSICO:\n")
    respuesta_basica = motor.generar_respuesta(prompt_basico)
    if respuesta_basica.startswith("[MODO RESPALDO]"):
        print(construir_respuesta_respaldo_pedido(pedido_encontrado, numero_seguimiento))
    else:
        print(respuesta_basica)

    imprimir_separador()

    print("PROMPT MEJORADO:\n")
    print(prompt_mejorado)

    imprimir_separador()

    print("RESPUESTA AL PROMPT MEJORADO:\n")
    respuesta_mejorada = motor.generar_respuesta(prompt_mejorado)
    if respuesta_mejorada.startswith("[MODO RESPALDO]"):
        print(construir_respuesta_respaldo_pedido(pedido_encontrado, numero_seguimiento))
    else:
        print(respuesta_mejorada)


def comparar_prompts_devolucion(
    motor: MotorGenerativoEcoMarket,
    nombre_producto: str,
    categoria_producto: str,
    dias_desde_entrega: int,
    con_empaque_original: bool,
    producto_defectuoso: bool,
    politicas_devolucion: Dict[str, Dict]
) -> None:
    documento_politicas = generar_documento_politicas(politicas_devolucion)
    evaluacion_previa = evaluar_devolucion(
        nombre_producto=nombre_producto,
        categoria_producto=categoria_producto,
        dias_desde_entrega=dias_desde_entrega,
        con_empaque_original=con_empaque_original,
        producto_defectuoso=producto_defectuoso,
        politicas_devolucion=politicas_devolucion
    )

    prompt_basico = construir_prompt_basico_devolucion(
        nombre_producto=nombre_producto,
        categoria_producto=categoria_producto,
        documento_politicas=documento_politicas
    )

    prompt_mejorado = construir_prompt_mejorado_devolucion(
        nombre_producto=nombre_producto,
        categoria_producto=categoria_producto,
        dias_desde_entrega=dias_desde_entrega,
        con_empaque_original=con_empaque_original,
        producto_defectuoso=producto_defectuoso,
        documento_politicas=documento_politicas,
        evaluacion_previa=evaluacion_previa
    )

    print("PROMPT BÁSICO:\n")
    print(prompt_basico)

    imprimir_separador()

    print("RESPUESTA AL PROMPT BÁSICO:\n")
    respuesta_basica = motor.generar_respuesta(prompt_basico)
    if respuesta_basica.startswith("[MODO RESPALDO]"):
        print(construir_respuesta_respaldo_devolucion(evaluacion_previa))
    else:
        print(respuesta_basica)

    imprimir_separador()

    print("PROMPT MEJORADO:\n")
    print(prompt_mejorado)

    imprimir_separador()

    print("RESPUESTA AL PROMPT MEJORADO:\n")
    respuesta_mejorada = motor.generar_respuesta(prompt_mejorado)
    if respuesta_mejorada.startswith("[MODO RESPALDO]"):
        print(construir_respuesta_respaldo_devolucion(evaluacion_previa))
    else:
        print(respuesta_mejorada)


def consultar_estado_pedido(
    motor: MotorGenerativoEcoMarket,
    numero_seguimiento: str,
    base_pedidos: List[Dict],
    indice_pedidos: Dict[str, Dict]
) -> None:
    documento_pedidos = generar_documento_pedidos(base_pedidos)
    pedido_encontrado = buscar_pedido(numero_seguimiento, indice_pedidos)

    prompt = construir_prompt_mejorado_pedido(
        numero_seguimiento=numero_seguimiento,
        documento_pedidos=documento_pedidos,
        pedido_encontrado=pedido_encontrado
    )

    respuesta = motor.generar_respuesta(prompt)

    print("\nRESPUESTA FINAL:\n")
    if respuesta.startswith("[MODO RESPALDO]"):
        print(construir_respuesta_respaldo_pedido(pedido_encontrado, numero_seguimiento))
    else:
        print(respuesta)
    print()


def consultar_devolucion(
    motor: MotorGenerativoEcoMarket,
    nombre_producto: str,
    categoria_producto: str,
    dias_desde_entrega: int,
    con_empaque_original: bool,
    producto_defectuoso: bool,
    politicas_devolucion: Dict[str, Dict]
) -> None:
    documento_politicas = generar_documento_politicas(politicas_devolucion)
    evaluacion_previa = evaluar_devolucion(
        nombre_producto=nombre_producto,
        categoria_producto=categoria_producto,
        dias_desde_entrega=dias_desde_entrega,
        con_empaque_original=con_empaque_original,
        producto_defectuoso=producto_defectuoso,
        politicas_devolucion=politicas_devolucion
    )

    prompt = construir_prompt_mejorado_devolucion(
        nombre_producto=nombre_producto,
        categoria_producto=categoria_producto,
        dias_desde_entrega=dias_desde_entrega,
        con_empaque_original=con_empaque_original,
        producto_defectuoso=producto_defectuoso,
        documento_politicas=documento_politicas,
        evaluacion_previa=evaluacion_previa
    )

    respuesta = motor.generar_respuesta(prompt)

    print("\nRESPUESTA FINAL:\n")
    if respuesta.startswith("[MODO RESPALDO]"):
        print(construir_respuesta_respaldo_devolucion(evaluacion_previa))
    else:
        print(respuesta)
    print()


def leer_booleano(mensaje: str) -> bool:
    valor = input(mensaje).strip().lower()
    return valor in ["si", "sí", "s", "1", "true", "verdadero"]


def mostrar_menu() -> None:
    print("ECO MARKET - TALLER PRÁCTICO #1")
    print("1. Generar archivos Markdown y datos de la entrega")
    print("2. Comparar prompt básico vs mejorado para estado de pedido")
    print("3. Comparar prompt básico vs mejorado para devolución")
    print("4. Consultar estado de pedido")
    print("5. Consultar devolución de producto")
    print("0. Salir")


def ejecutar_aplicacion() -> None:
    base_pedidos = cargar_base_pedidos()
    politicas_devolucion = cargar_politicas_devolucion()
    catalogo_productos = cargar_catalogo_productos()

    indice_pedidos = crear_indice_pedidos(base_pedidos)
    indice_productos = crear_indice_productos(catalogo_productos)

    motor = MotorGenerativoEcoMarket()
    motor.cargar_modelo()

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            generar_archivos_markdown_y_datos()

        elif opcion == "2":
            numero_seguimiento = input("Ingresa el número de seguimiento (ejemplo: EM-1004): ").strip().upper()
            comparar_prompts_pedido(
                motor=motor,
                numero_seguimiento=numero_seguimiento,
                base_pedidos=base_pedidos,
                indice_pedidos=indice_pedidos
            )

        elif opcion == "3":
            nombre_producto = input("Nombre del producto: ").strip()

            producto_catalogo = buscar_producto(nombre_producto, indice_productos)
            if producto_catalogo:
                categoria_producto = producto_catalogo["categoria"]
                print(f"Categoría detectada automáticamente: {categoria_producto}")
            else:
                categoria_producto = input("No se encontró el producto. Ingresa la categoría manualmente: ").strip().lower()

            dias_desde_entrega = int(input("Días desde la entrega: ").strip())
            con_empaque_original = leer_booleano("¿Conserva empaque original? (si/no): ")
            producto_defectuoso = leer_booleano("¿El producto presenta defecto? (si/no): ")

            comparar_prompts_devolucion(
                motor=motor,
                nombre_producto=nombre_producto,
                categoria_producto=categoria_producto,
                dias_desde_entrega=dias_desde_entrega,
                con_empaque_original=con_empaque_original,
                producto_defectuoso=producto_defectuoso,
                politicas_devolucion=politicas_devolucion
            )

        elif opcion == "4":
            numero_seguimiento = input("Ingresa el número de seguimiento: ").strip().upper()
            consultar_estado_pedido(
                motor=motor,
                numero_seguimiento=numero_seguimiento,
                base_pedidos=base_pedidos,
                indice_pedidos=indice_pedidos
            )

        elif opcion == "5":
            nombre_producto = input("Nombre del producto: ").strip()

            producto_catalogo = buscar_producto(nombre_producto, indice_productos)
            if producto_catalogo:
                categoria_producto = producto_catalogo["categoria"]
                print(f"Categoría detectada automáticamente: {categoria_producto}")
            else:
                categoria_producto = input("No se encontró el producto. Ingresa la categoría manualmente: ").strip().lower()

            dias_desde_entrega = int(input("Días desde la entrega: ").strip())
            con_empaque_original = leer_booleano("¿Conserva empaque original? (si/no): ")
            producto_defectuoso = leer_booleano("¿El producto presenta defecto? (si/no): ")

            consultar_devolucion(
                motor=motor,
                nombre_producto=nombre_producto,
                categoria_producto=categoria_producto,
                dias_desde_entrega=dias_desde_entrega,
                con_empaque_original=con_empaque_original,
                producto_defectuoso=producto_defectuoso,
                politicas_devolucion=politicas_devolucion
            )

        elif opcion == "0":
            print("\nPrograma finalizado.\n")
            break

        else:
            print("\nOpción no válida. Intenta nuevamente.\n")


if __name__ == "__main__":
    ejecutar_aplicacion()