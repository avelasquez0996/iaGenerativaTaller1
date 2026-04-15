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

## Enfoque
Se usa una solución híbrida:
- contexto estructurado,
- reglas de negocio,
- modelo open-source instruct,
- escalamiento humano cuando sea necesario.