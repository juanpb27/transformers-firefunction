from fastapi import FastAPI, Request
import json
from app.model import load_model
from app.config import function_spec

app = FastAPI()

# Cargar el modelo y el tokenizer
model, tokenizer = load_model()

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    request_data = await request.json()
    messages = request_data.get("messages", [])

    # Agregar las funciones al chat
    messages.insert(0, {'role': 'functions', 'content': json.dumps(function_spec, indent=4)})
    model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)

    # Generar respuesta
    generated_ids = model.generate(model_inputs['input_ids'], max_new_tokens=128)
    decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

    return {"response": decoded[0]}
