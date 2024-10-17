from fastapi import FastAPI, Request
from app.model import load_model
from app.config import function_spec
import json

app = FastAPI()

# Cargar el modelo y el tokenizer
model, tokenizer = load_model()

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    # Obtener el contenido del mensaje desde el JSON de la petición
    request_data = await request.json()
    user_message = request_data.get("message", "")

    # Definir la estructura de los mensajes con las funciones
    functions = json.dumps(function_spec, indent=4)
    messages = [
        {'role': 'functions', 'content': functions},
        {'role': 'system', 'content': 'You are a helpful assistant with access to functions. Use them if required.'},
        {'role': 'user', 'content': user_message}
    ]

    # Procesar la solicitud a través del modelo
    model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)

    # Generar la respuesta del modelo
    generated_ids = model.generate(model_inputs['input_ids'], max_new_tokens=128)
    decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

    # Respuesta generada por el modelo
    return {"response": decoded[0]}
