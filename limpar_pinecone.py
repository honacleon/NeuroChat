import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Importar Pinecone
try:
    from pinecone import Pinecone
except ImportError:
    import pinecone
    Pinecone = None

def limpar_pinecone():
    """Limpar completamente o índice Pinecone"""
    
    # Configurações do .env
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME", "firstry")
    
    if not api_key:
        print("❌ ERRO: PINECONE_API_KEY não encontrada no .env")
        return
    
    try:
        # Conectar ao Pinecone
        if Pinecone is not None:
            # Versão nova
            pc = Pinecone(api_key=api_key)
            index = pc.Index(index_name)
        else:
            # Versão antiga
            pinecone.init(api_key=api_key)
            index = pinecone.Index(index_name)
        
        print(f"🔗 Conectado ao índice: {index_name}")
        
        # Verificar status antes
        stats_antes = index.describe_index_stats()
        total_antes = stats_antes.get('total_vector_count', 0)
        print(f"📊 Vetores antes da limpeza: {total_antes}")
        
        if total_antes == 0:
            print("✅ Índice já está vazio!")
            return
        
        # CONFIRMAÇÃO DE SEGURANÇA
        confirmacao = input(f"\n⚠️  ATENÇÃO: Isso vai DELETAR TODOS os {total_antes} vetores do índice '{index_name}'!\n🤔 Tem certeza? Digite 'SIM' para confirmar: ")
        
        if confirmacao.upper() != 'SIM':
            print("❌ Operação cancelada pelo usuário")
            return
        
        print("\n🗑️ Iniciando limpeza...")
        
        # DELETAR TUDO
        index.delete(delete_all=True)
        
        print("⏳ Aguardando limpeza...")
        import time
        time.sleep(5)  # Aguardar processamento
        
        # Verificar status depois
        stats_depois = index.describe_index_stats()
        total_depois = stats_depois.get('total_vector_count', 0)
        
        print(f"\n✅ LIMPEZA CONCLUÍDA!")
        print(f"📊 Vetores depois: {total_depois}")
        print(f"🗑️ Removidos: {total_antes - total_depois}")
        
        if total_depois == 0:
            print("🎉 Índice completamente limpo!")
        else:
            print("⚠️ Alguns vetores ainda estão sendo processados...")
        
    except Exception as e:
        print(f"❌ ERRO: {e}")

if __name__ == "__main__":
    print("🧹 LIMPADOR DE ÍNDICE PINECONE")
    print("=" * 40)
    limpar_pinecone()