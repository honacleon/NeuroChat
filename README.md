# NeuroChat AI – Chatbot RAG com Streamlit, OpenAI e Pinecone

## 🚀 Visão Geral

O **NeuroChat AI** é um chatbot inteligente baseado em RAG (Retrieval-Augmented Generation), que combina modelos de linguagem da OpenAI, banco vetorial Pinecone e uma interface web futurista com Streamlit. O sistema permite consultar grandes volumes de documentos (PDFs convertidos) de forma semântica, respondendo perguntas com contexto e precisão.

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **OpenAI (API)**: Geração de embeddings e respostas contextuais usando modelos de última geração (GPT-4o, text-embedding-3-small).
- **Pinecone**: Banco vetorial para indexação e busca semântica de documentos.
- **LangChain**: Pipeline para chunking, preparação e manipulação de documentos.
- **Streamlit**: Interface web moderna, responsiva e customizada com CSS avançado.
- **Python-dotenv**: Gerenciamento seguro de variáveis de ambiente.
- **PDF Converter**: Pipeline para converter PDFs em TXT/JSON, facilitando ingestão de dados.
- **Design Futurista**: UI diferenciada com animações, gradientes, fontes customizadas e experiência de usuário avançada.

## 🧠 Como Funciona

1. **Conversão de PDFs**: Use o script `pdf_converter.py` para transformar arquivos PDF em TXT/JSON.
2. **Processamento e Indexação**: Rode `rag_system.py` para dividir documentos em chunks, gerar embeddings via OpenAI e indexar tudo no Pinecone.
3. **Chatbot Inteligente**: Execute `chatbot_streamlit.py` para acessar a interface web. O chatbot busca respostas nos documentos indexados, usando RAG para trazer contexto real e respostas precisas.

## 📦 Estrutura do Projeto

```
├── chatbot_streamlit.py   # Interface web e chatbot RAG
├── rag_system.py          # Pipeline de chunking, embedding e indexação
├── pdf_converter.py       # Conversão de PDF para TXT/JSON
├── requirements.txt       # Dependências do projeto
├── output/                # Pasta padrão para arquivos TXT/JSON convertidos
├── .env                   # Variáveis de ambiente (API keys)
```



## 💡 Demonstração de Uso

- Faça uma pergunta no chat e veja respostas contextuais baseadas nos seus documentos.
- Visualize estatísticas em tempo real (número de vetores, dimensões, histórico de consultas).
- Experimente o design futurista e a experiência de usuário diferenciada.

## ✨ Diferenciais Técnicos

- **RAG Completo**: Pipeline de ingestão, chunking, embeddings, indexação e busca semântica.
- **Integração Profunda**: OpenAI + Pinecone + LangChain + Streamlit.
- **UX/UI Premium**: CSS customizado, animações, responsividade e experiência imersiva.
- **Automação**: Scripts independentes para cada etapa do fluxo.
- **Pronto para escalar**: Basta adicionar novos PDFs, reprocessar e consultar!

## 📢 Sobre o Autor

Desenvolvido por [Honacleon Junior] – apaixonado por IA, NLP e soluções inovadoras. Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/honacleon/)!

---

> ⭐️ Se gostou, deixe uma estrela no repositório e compartilhe no LinkedIn!

---

**Powered by:** OpenAI • Pinecone • LangChain • Streamlit
