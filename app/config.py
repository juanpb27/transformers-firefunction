import os

# Cargar variables de entorno desde el archivo .env
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", 8000))

# Definir las funciones
function_spec = [
    {
        "name": "obtener_hora_actual",
        "description": "Devuelve la hora actual en formato HH:MM:SS.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "convertir_moneda",
        "description": "Convierte una cantidad de dinero de una moneda a otra.",
        "parameters": {
            "type": "object",
            "properties": {
                "cantidad": {
                    "type": "number",
                    "description": "Cantidad de dinero a convertir"
                },
                "moneda_origen": {
                    "type": "string",
                    "description": "Código de la moneda origen, por ejemplo: USD, EUR, COP"
                },
                "moneda_destino": {
                    "type": "string",
                    "description": "Código de la moneda destino, por ejemplo: USD, EUR, COP"
                }
            },
            "required": ["cantidad", "moneda_origen", "moneda_destino"]
        }
    }
]