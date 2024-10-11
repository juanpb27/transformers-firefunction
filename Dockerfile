FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; AutoModelForCausalLM.from_pretrained('fireworks-ai/firefunction-v1'); AutoTokenizer.from_pretrained('fireworks-ai/firefunction-v1')"

EXPOSE 8000

CMD ["python", "main.py"]
