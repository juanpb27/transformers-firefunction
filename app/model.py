from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model():
    model = AutoModelForCausalLM.from_pretrained("fireworks-ai/firefunction-v1")
    tokenizer = AutoTokenizer.from_pretrained("fireworks-ai/firefunction-v1")
    return model, tokenizer
