# Transformers FireFunction

## Descripción

Este proyecto utiliza el modelo **FireFunction v1** con la librería **Transformers** y está implementado usando **FastAPI** para construir un servidor que expone un endpoint para realizar inferencias con el modelo. Se puede ejecutar tanto de forma local como mediante contenedores Docker.

## Instalación

#### 1. Clonar el repositorio

```bash
git clone https://github.com/juanpb27/transformers-firefunction.git
cd transformers-firefunction
```

#### 2. Construir y levantar el contenedor usando Docker Compose
```bash
docker-compose up --build
```

Esto construirá la imagen del contenedor y levantará el servidor FastAPI.

3. Probar la aplicación
Puedes probar la aplicación utilizando curl o alguna herramienta como Postman. Aquí un ejemplo de un curl:

```bash
curl -X POST "http://localhost:8000/v1/chat/completions" \
     -H "Content-Type: application/json" \
     --data '{
         "model": "fireworks-ai/firefunction-v1",
         "messages": [
             {"role": "user", "content": "Convierte 100 USD a EUR."}
         ],
         "function_call": {
             "name": "convertir_moneda",
             "arguments": {
                 "cantidad": 100,
                 "moneda_origen": "USD",
                 "moneda_destino": "EUR"
             }
         }
     }'
```