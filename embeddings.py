import ollama

# 1. Frase curta em português para gerar o embedding
texto_exemplo = "A tokenização divide o texto, e os embeddings geram os vetores."

# 2. Modelo de alta dimensão utilizado na aula do professor
modelo_utilizado = "mxbai-embed-large"

print(f"Texto de entrada: '{texto_exemplo}'")
print(f"Utilizando o modelo: '{modelo_utilizado}'\n")

try:
    # 3. Executa a chamada ao Ollama local
    resposta = ollama.embeddings(model=modelo_utilizado, prompt=texto_exemplo)
    vetor_embeddings = resposta['embedding']
    
    # 4. Exibe o sumário solicitado nos critérios da atividade
    print("=== Sucesso na Geração ===")
    print(f"Dimensão (tamanho do vetor): {len(vetor_embeddings)}")
    print(f"Primeiros 5 valores do vetor: {vetor_embeddings[:5]}")

except Exception as e:
    print(f"Erro ao conectar ao Ollama local: {e}")
    print("Dica: Certifique-se de ter rodado 'ollama pull mxbai-embed-large' no terminal.")
