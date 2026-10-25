# Avaliação Online 3 - Geração de Embeddings com Ollama

Este projeto demonstra a instalação, configuração e operação local do Ollama para a geração de vetores de embeddings a partir de textos em português utilizando Python.

## Requisitos e Tecnologias
* Python 3.10+
* Ollama instalado localmente
* Modelo: `mxbai-embed-large`

## Como Executar o Projeto

1. **Instalar o Ollama e o Modelo:**
   Certificar-se de que o Ollama está rodando na máquina e baixar o modelo pelo terminal:
   ```
   ollama pull mxbai-embed-large
   ```

2. **Configurar o Ambiente Python:**
   Instalar a biblioteca oficial do Ollama:
   ```
   pip install ollama
   ```

3. **Executar o Script:**
   Rodar o script principal para gerar e visualizar os embeddings:
   ```
   python embeddings.py
   ```
