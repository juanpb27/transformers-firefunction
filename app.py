import subprocess

def run_vllm():
    # Comando para ejecutar el modelo usando vLLM
    subprocess.run(["vllm", "serve", "fireworks-ai/firefunction-v1"])

if __name__ == "__main__":
    print("Iniciando el servidor vLLM...")
    run_vllm()
