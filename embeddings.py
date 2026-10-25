import ollama

# 1. Uma frase curta em português para gerar o embedding
texto_exemplo = "A tokenização divide o texto, e os embeddings geram os vetores."

# 2. Modelo de alta dimensão utilizado para gerar embeddings
modelo_utilizado = "mxbai-embed-large"

print(f"Texto de entrada: '{texto_exemplo}'")
print(f"Utilizando o modelo: '{modelo_utilizado}'\n")

try:
    # 3. Executa a chamada ao Ollama local
    resposta = ollama.embeddings(model=modelo_utilizado, prompt=texto_exemplo)
    vetor_embeddings = resposta['embedding']
    
    # 4. Exibe o sumário do embedding gerado
    print("=== Sucesso na Geração ===")
    print(f"Dimensão (tamanho do vetor): {len(vetor_embeddings)}")
    print(f"Primeiros 5 valores do vetor: {vetor_embeddings[:5]}")

except Exception as e:
    print(f"Erro ao conectar ao Ollama local: {e}")
    print("Dica: Certificar-se de ter rodado 'ollama pull mxbai-embed-large' no terminal.")
