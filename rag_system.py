import os
import json
from pathlib import Path
from typing import List, Dict
import time

# Carregar variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()

# Importações para processamento de texto
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Importações para embeddings
import openai
from openai import OpenAI

# Importações para Pinecone
from pinecone import Pinecone, ServerlessSpec

class DocumentProcessor:
    """Classe para processar documentos e criar sistema RAG"""
    
    def __init__(self, openai_api_key: str, pinecone_api_key: str):
        """
        Inicializar processador
        
        Args:
            openai_api_key: Chave API da OpenAI
            pinecone_api_key: Chave API do Pinecone
        """
        # Configurar OpenAI
        self.openai_client = OpenAI(api_key=openai_api_key)
        
        # Configurar Pinecone
        self.pc = Pinecone(api_key=pinecone_api_key)
        
        # Configurações do chunking
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,        # Tamanho do chunk
            chunk_overlap=200,      # Sobreposição entre chunks
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        
    def load_documents(self, folder_path: str) -> List[Document]:
        """
        Carregar documentos TXT da pasta
        
        Args:
            folder_path: Caminho para pasta com arquivos TXT
            
        Returns:
            Lista de documentos do LangChain
        """
        documents = []
        txt_files = Path(folder_path).glob("*.txt")
        
        for txt_file in txt_files:
            print(f"📖 Carregando: {txt_file.name}")
            
            with open(txt_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Criar documento com metadados
            doc = Document(
                page_content=content,
                metadata={
                    "source": str(txt_file),
                    "filename": txt_file.name,
                    "file_size": len(content)
                }
            )
            documents.append(doc)
            
        print(f"✅ {len(documents)} documentos carregados")
        return documents
    
    def create_chunks(self, documents: List[Document]) -> List[Document]:
        """
        Dividir documentos em chunks
        
        Args:
            documents: Lista de documentos
            
        Returns:
            Lista de chunks
        """
        print("🔪 Criando chunks...")
        
        all_chunks = []
        for doc in documents:
            chunks = self.text_splitter.split_documents([doc])
            
            # Adicionar ID único para cada chunk
            for i, chunk in enumerate(chunks):
                chunk.metadata.update({
                    "chunk_id": f"{doc.metadata['filename']}_{i}",
                    "chunk_index": i,
                    "total_chunks": len(chunks)
                })
                
            all_chunks.extend(chunks)
            print(f"  📄 {doc.metadata['filename']}: {len(chunks)} chunks")
            
        print(f"✅ Total de {len(all_chunks)} chunks criados")
        return all_chunks
    
    def create_embeddings(self, chunks: List[Document]) -> List[Dict]:
        """
        Criar embeddings para os chunks
        
        Args:
            chunks: Lista de chunks
            
        Returns:
            Lista de embeddings com metadados
        """
        print("🧠 Criando embeddings...")
        
        embeddings_data = []
        batch_size = 10  # Processar em lotes para evitar rate limits
        
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            print(f"  🔄 Processando lote {i//batch_size + 1}/{(len(chunks)-1)//batch_size + 1}")
            
            # Criar embeddings para o lote
            texts = [chunk.page_content for chunk in batch]
            
            try:
                response = self.openai_client.embeddings.create(
                    model="text-embedding-3-small",  # Modelo mais econômico
                    input=texts
                )
                
                # Processar resposta
                for j, chunk in enumerate(batch):
                    embedding_data = {
                        "id": chunk.metadata["chunk_id"],
                        "values": response.data[j].embedding,
                        "metadata": {
                            **chunk.metadata,
                            "text": chunk.page_content[:1000]  # Primeiros 1000 chars para preview
                        }
                    }
                    embeddings_data.append(embedding_data)
                    
                # Pequena pausa para evitar rate limits
                time.sleep(0.5)
                
            except Exception as e:
                print(f"❌ Erro ao criar embeddings: {e}")
                continue
                
        print(f"✅ {len(embeddings_data)} embeddings criados")
        return embeddings_data
    
    def setup_pinecone_index(self, index_name: str = "documentos-rag") -> str:
        """
        Configurar índice no Pinecone
        
        Args:
            index_name: Nome do índice
            
        Returns:
            Nome do índice criado
        """
        print(f"🌲 Configurando índice Pinecone: {index_name}")
        
        # Verificar se índice já existe
        existing_indexes = [index.name for index in self.pc.list_indexes()]
        
        if index_name in existing_indexes:
            print(f"  ℹ️ Índice '{index_name}' já existe")
            # Deletar índice existente (opcional - remova se quiser manter dados)
            print(f"  🗑️ Deletando índice existente...")
            self.pc.delete_index(index_name)
            time.sleep(10)  # Aguardar deleção
        
        # Criar novo índice
        print(f"  🔨 Criando novo índice...")
        self.pc.create_index(
            name=index_name,
            dimension=1536,  # Dimensão do text-embedding-3-small
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
        
        # Aguardar índice ficar pronto
        print("  ⏳ Aguardando índice ficar pronto...")
        while not self.pc.describe_index(index_name).status['ready']:
            time.sleep(5)
            
        print(f"✅ Índice '{index_name}' criado e pronto!")
        return index_name
    
    def upload_to_pinecone(self, embeddings_data: List[Dict], index_name: str):
        """
        Fazer upload dos embeddings para Pinecone
        
        Args:
            embeddings_data: Lista de embeddings
            index_name: Nome do índice
        """
        print(f"📤 Fazendo upload para Pinecone...")
        
        # Conectar ao índice
        index = self.pc.Index(index_name)
        
        # Upload em lotes
        batch_size = 100
        for i in range(0, len(embeddings_data), batch_size):
            batch = embeddings_data[i:i + batch_size]
            
            try:
                index.upsert(vectors=batch)
                print(f"  ✅ Lote {i//batch_size + 1}/{(len(embeddings_data)-1)//batch_size + 1} enviado")
                time.sleep(1)  # Pequena pausa
                
            except Exception as e:
                print(f"  ❌ Erro no lote {i//batch_size + 1}: {e}")
                continue
        
        # Verificar estatísticas do índice
        time.sleep(5)  # Aguardar indexação
        stats = index.describe_index_stats()
        print(f"📊 Estatísticas do índice:")
        print(f"  • Total de vetores: {stats['total_vector_count']}")
        print(f"  • Dimensão: {stats['dimension']}")
        
    def process_documents_to_pinecone(self, folder_path: str, index_name: str = "documentos-rag"):
        """
        Processo completo: documentos → chunks → embeddings → Pinecone
        
        Args:
            folder_path: Pasta com arquivos TXT
            index_name: Nome do índice Pinecone
        """
        print("🚀 Iniciando processo completo RAG...")
        start_time = time.time()
        
        # 1. Carregar documentos
        documents = self.load_documents(folder_path)
        
        # 2. Criar chunks
        chunks = self.create_chunks(documents)
        
        # 3. Criar embeddings
        embeddings_data = self.create_embeddings(chunks)
        
        # 4. Configurar Pinecone
        index_name = self.setup_pinecone_index(index_name)
        
        # 5. Upload para Pinecone
        self.upload_to_pinecone(embeddings_data, index_name)
        
        total_time = time.time() - start_time
        print(f"\n🎉 PROCESSO CONCLUÍDO!")
        print(f"⏱️ Tempo total: {total_time:.2f} segundos")
        print(f"📁 Documentos processados: {len(documents)}")
        print(f"🔪 Chunks criados: {len(chunks)}")
        print(f"🧠 Embeddings gerados: {len(embeddings_data)}")
        print(f"🌲 Índice Pinecone: {index_name}")

def main():
    """Função principal"""
    
    # CARREGAR CONFIGURAÇÕES DO .env
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    DOCUMENTS_FOLDER = os.getenv("DOCUMENTS_FOLDER", "output")
    
    # Usar PINECONE_INDEX_NAME se disponível, senão INDEX_NAME
    INDEX_NAME = os.getenv("PINECONE_INDEX_NAME") or os.getenv("INDEX_NAME", "documentos-rag")
    
    print("🔧 Configurações carregadas:")
    print(f"  📁 Pasta de documentos: {DOCUMENTS_FOLDER}")
    print(f"  🌲 Nome do índice: {INDEX_NAME}")
    print(f"  🤖 Modelo OpenAI: {os.getenv('OPENAI_MODEL', 'text-embedding-3-small')}")
    
    # Verificar se as chaves foram configuradas
    if not OPENAI_API_KEY or not PINECONE_API_KEY:
        print("\n❌ ERRO: Chaves API não configuradas!")
        print("📝 COMO CONFIGURAR:")
        print("1. Crie um arquivo .env na pasta do projeto")
        print("2. Adicione suas chaves:")
        print("   OPENAI_API_KEY=sk-proj-xxxxxxxx")
        print("   PINECONE_API_KEY=pcsk_xxxxxxxx")
        print("\n🔗 Links para obter as chaves:")
        print("• OpenAI: https://platform.openai.com/api-keys")
        print("• Pinecone: https://app.pinecone.io/")
        return
    
    # Verificar se a pasta existe
    if not Path(DOCUMENTS_FOLDER).exists():
        print(f"❌ ERRO: Pasta '{DOCUMENTS_FOLDER}' não encontrada!")
        print(f"📁 Verifique se a pasta existe e contém arquivos .txt")
        return
    
    # Verificar se existem arquivos TXT
    txt_files = list(Path(DOCUMENTS_FOLDER).glob("*.txt"))
    if not txt_files:
        print(f"❌ ERRO: Nenhum arquivo .txt encontrado em '{DOCUMENTS_FOLDER}'!")
        return
        
    print(f"📄 Encontrados {len(txt_files)} arquivos TXT:")
    for txt_file in txt_files:
        size_kb = txt_file.stat().st_size / 1024
        print(f"  • {txt_file.name} ({size_kb:.1f} KB)")
    
    # Verificar se o índice já existe
    try:
        pc = Pinecone(api_key=PINECONE_API_KEY)
        existing_indexes = [index.name for index in pc.list_indexes()]
        
        if INDEX_NAME in existing_indexes:
            print(f"\n📋 Índice '{INDEX_NAME}' já existe no Pinecone!")
            choice = input("Deseja usar o existente (s) ou recriar (n)? [s/n]: ").lower()
            
            if choice == 'n':
                print(f"🗑️ Deletando índice existente...")
                pc.delete_index(INDEX_NAME)
                time.sleep(10)
                print("✅ Índice deletado!")
            else:
                print("✅ Usando índice existente!")
                
    except Exception as e:
        print(f"⚠️ Erro ao verificar índices: {e}")
    
    try:
        # Criar processador
        processor = DocumentProcessor(OPENAI_API_KEY, PINECONE_API_KEY)
        
        # Executar processo completo
        processor.process_documents_to_pinecone(DOCUMENTS_FOLDER, INDEX_NAME)
        
        print(f"\n🎯 PRÓXIMOS PASSOS:")
        print("1. ✅ Seus documentos estão no Pinecone!")
        print("2. 🤖 Agora você pode criar o chatbot")
        print("3. 💬 Use busca semântica para responder perguntas")
        print(f"4. 📋 Índice criado: {INDEX_NAME}")
        print(f"5. 🌐 Host Pinecone: {os.getenv('PINECONE_HOST', 'Auto-detectado')}")
        
    except Exception as e:
        print(f"❌ Erro durante o processo: {e}")
        print("🔍 Verifique:")
        print("• Chaves API válidas (TROQUE AS EXPOSTAS!)")
        print("• Conexão com internet")
        print("• Créditos na OpenAI")

if __name__ == "__main__":
    main()