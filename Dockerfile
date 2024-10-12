FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir --timeout=300 -r requirements.txt

COPY . .

RUN python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; AutoModelForCausalLM.from_pretrained('fireworks-ai/firefunction-v1'); AutoTokenizer.from_pretrained('fireworks-ai/firefunction-v1')"

EXPOSE 8000

CMD ["python", "main.py"]
