from fastapi import FastAPI, Request
from app.model import load_model
from app.config import function_spec
import json

app = FastAPI()

# Cargar el modelo y el tokenizer
model, tokenizer = load_model()

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    request_data = await request.json()
    messages = request_data.get("messages", [])

    # Agregar las funciones disponibles al mensaje inicial
    functions = json.dumps(function_spec, indent=4)
    messages.insert(0, {'role': 'functions', 'content': functions})

    # Procesar la solicitud a través del modelo
    model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
    generated_ids = model.generate(model_inputs['input_ids'], max_new_tokens=128)
    decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

    # Respuesta generada por el modelo
    return {"response": decoded[0]}