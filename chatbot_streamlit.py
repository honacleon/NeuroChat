import streamlit as st
import os
from typing import List, Dict
import time
import random

# Carregar variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()

# Mock responses para demonstração
DEMO_RESPONSES = [
    "🤖 **Esta é uma demonstração do NeuroChat AI!** \n\nEsta versão é apenas para mostrar a interface futurística e as funcionalidades. Para usar o sistema completo com busca em documentos reais, você precisa:\n\n• Configurar sua própria chave do Pinecone\n• Configurar sua chave do Google Gemini\n• Fazer upload dos seus documentos\n\nO design foi criado para proporcionar uma experiência visual imersiva com gradientes neon, animações e efeitos holográficos!",
    
    "⚡ **Sistema Neural em Modo Demo** \n\nEsta interface demonstra como seria a experiência real do NeuroChat AI. O sistema real seria capaz de:\n\n• Processar documentos PDF, TXT, DOCX\n• Criar embeddings vetoriais inteligentes\n• Realizar buscas semânticas avançadas\n• Gerar respostas contextualizadas com IA\n\nTudo isso com esta interface cyberpunk incrível!",
    
    "🧠 **Exemplo de Resposta Neural** \n\nEm um ambiente real, o NeuroChat processaria sua pergunta através de:\n\n1. **Análise Semântica**: Compreendendo o significado profundo\n2. **Busca Vetorial**: Encontrando conteúdo relevante nos documentos\n3. **Síntese Inteligente**: Combinando informações de múltiplas fontes\n4. **Resposta Contextual**: Gerando uma resposta precisa e útil\n\nA magia acontece em milissegundos! ⚡",
    
    "🚀 **Demo: Capacidades do Sistema** \n\nO NeuroChat AI real seria capaz de responder perguntas como:\n\n• \"Quais são os principais tópicos dos documentos?\"\n• \"Encontre informações sobre X no arquivo Y\"\n• \"Resuma os pontos importantes do capítulo Z\"\n• \"Compare as diferentes abordagens mencionadas\"\n\nTudo isso processado por uma IA avançada com interface futurística!",
    
    "✨ **Demonstração Interativa** \n\nEsta é uma prévia do que seria possível com o sistema completo:\n\n🔍 **Busca Inteligente**: Encontra informações mesmo com perguntas complexas\n🎯 **Respostas Precisas**: Combina múltiplas fontes de forma coerente\n⚡ **Processamento Rápido**: Segundos para analisar grandes volumes de dados\n🎨 **Interface Imersiva**: Experiência visual única e envolvente\n\nUma verdadeira revolução em busca de documentos!"
]

class DemoGeminiRAGChatbot:
    """Versão Demo do Chatbot RAG - Apenas para demonstração"""
    
    def __init__(self):
        """Inicializar chatbot em modo demo"""
        self.demo_mode = True
        self.total_vectors = random.randint(15000, 25000)
        self.dimensions = 768
        
        # Simular conexão bem-sucedida
        st.success(f"✅ Conectado (DEMO): {self.total_vectors:,} chunks simulados")
    
    def ask_question(self, question: str) -> str:
        """Simular resposta para demo"""
        try:
            # Simular processamento
            time.sleep(random.uniform(1.2, 2.5))
            
            # Escolher resposta aleatória baseada na pergunta
            if any(word in question.lower() for word in ['autor', 'quem', 'criador']):
                return "📝 **Em um sistema real**, eu analisaria os metadados dos documentos para identificar autores, datas de criação e outras informações relevantes. Esta é uma demonstração da interface - configure suas chaves API para funcionalidade completa!"
            
            elif any(word in question.lower() for word in ['resumo', 'resumir', 'principais']):
                return "📊 **Funcionalidade de Resumo (Demo)**: O sistema real extrairia os pontos principais de todos os documentos indexados, criaria um resumo inteligente e apresentaria as informações mais relevantes. A interface que você está vendo funcionaria com dados reais!"
            
            elif any(word in question.lower() for word in ['como', 'tutorial', 'exemplo']):
                return "🎓 **Tutorial Demo**: Esta interface mostra como seria usar o NeuroChat AI real. Você faria perguntas naturais, o sistema buscaria em seus documentos usando IA avançada, e retornaria respostas contextualizadas como esta - mas com seus dados reais!"
            
            else:
                return random.choice(DEMO_RESPONSES)
                
        except Exception as e:
            return "🎭 **Modo Demonstração Ativo** - Esta é uma vitrine visual do NeuroChat AI. Configure as chaves API reais para funcionalidade completa!"

# =================== DESIGN FUTURÍSTICO ÉPICO ===================

# Configurar página com tema escuro
st.set_page_config(
    page_title="NeuroChat AI - Demo",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS FUTURÍSTICO COM GRADIENTES E ANIMAÇÕES
st.markdown("""
<style>
    /* IMPORTAR FONTE FUTURÍSTICA */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    /* TEMA ESCURO GLOBAL */
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #0c0c0c 100%);
        background-attachment: fixed;
    }
    
    /* EFEITO MATRIX ANIMADO NO FUNDO */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(120, 219, 255, 0.1) 0%, transparent 50%);
        animation: pulse 4s ease-in-out infinite alternate;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes pulse {
        0% { opacity: 0.3; }
        100% { opacity: 0.8; }
    }
    
    /* CONTAINER PRINCIPAL */
    .main > div {
        background: rgba(15, 15, 35, 0.8) !important;
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(120, 219, 255, 0.3);
        box-shadow: 0 8px 32px rgba(120, 219, 255, 0.1);
        padding: 20px;
        margin: 10px;
    }
    
    /* TÍTULOS COM GRADIENTE NEON */
    h1 {
        font-family: 'Orbitron', monospace !important;
        font-weight: 900 !important;
        font-size: 3.5rem !important;
        background: linear-gradient(45deg, #0066ff, #00ffff, #ff00ff, #ffff00);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: neon-gradient 3s ease-in-out infinite;
        text-align: center;
        text-shadow: 0 0 30px rgba(0, 245, 255, 0.5);
        margin-bottom: 10px !important;
    }
    
    @keyframes neon-gradient {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* SUBTÍTULO TECH */
    .subtitle {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.4rem;
        color: #78dbff;
        text-align: center;
        margin-bottom: 30px;
        opacity: 0.9;
        letter-spacing: 2px;
    }
    
    /* BOTÕES FUTURÍSTICOS */
    .stButton > button {
        background: linear-gradient(45deg, #0066ff, #00ffff) !important;
        border: none !important;
        border-radius: 15px !important;
        color: #000 !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        padding: 12px 30px !important;
        box-shadow: 0 5px 20px rgba(0, 255, 255, 0.3) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #00ffff, #ff00ff) !important;
        box-shadow: 0 8px 30px rgba(255, 0, 255, 0.4) !important;
        transform: translateY(-2px) !important;
    }
    
    /* CAMPOS DE INPUT CYBER */
    .stTextArea > div > div > textarea {
        background: rgba(0, 20, 40, 0.8) !important;
        border: 2px solid rgba(120, 219, 255, 0.3) !important;
        border-radius: 15px !important;
        color: #78dbff !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 1.1rem !important;
        backdrop-filter: blur(5px) !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #00ffff !important;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3) !important;
    }
    
    /* MÉTRICAS FUTURÍSTICAS */
    .metric-container {
        background: linear-gradient(135deg, rgba(0, 102, 255, 0.1), rgba(0, 255, 255, 0.1));
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 5px 20px rgba(0, 255, 255, 0.1);
    }
    
    /* CARDS DE RESPOSTA NEON */
    .response-card {
        background: linear-gradient(135deg, rgba(0, 255, 127, 0.1), rgba(0, 255, 255, 0.1));
        border: 2px solid rgba(0, 255, 127, 0.4);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0, 255, 127, 0.2);
        backdrop-filter: blur(10px);
        animation: glow-green 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow-green {
        0% { box-shadow: 0 10px 30px rgba(0, 255, 127, 0.2); }
        100% { box-shadow: 0 15px 40px rgba(0, 255, 127, 0.4); }
    }
    
    /* LOADING SPINNER CYBER */
    .stSpinner > div {
        border-color: #00ffff !important;
    }
    
    /* SIDEBAR TECH */
    .css-1d391kg {
        background: linear-gradient(180deg, #0c0c0c, #1a1a2e) !important;
    }
    
    /* SUCCESS/ERROR MESSAGES */
    .stAlert {
        backdrop-filter: blur(10px) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    
    /* EXPANDER FUTURÍSTICO */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, rgba(120, 219, 255, 0.1), rgba(255, 0, 255, 0.1)) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(120, 219, 255, 0.3) !important;
    }
    
    /* TEXTO TECH */
    .tech-text {
        font-family: 'Rajdhani', sans-serif;
        color: #78dbff;
        font-size: 1.2rem;
        font-weight: 500;
    }
    
    /* PULSING DOTS ANIMATION */
    .pulse-dot {
        height: 10px;
        width: 10px;
        background: #00ffff;
        border-radius: 50%;
        display: inline-block;
        margin: 0 2px;
        animation: pulse-dot 1.5s infinite ease-in-out;
    }
    
    .pulse-dot:nth-child(2) { animation-delay: 0.3s; }
    .pulse-dot:nth-child(3) { animation-delay: 0.6s; }
    
    @keyframes pulse-dot {
        0%, 60%, 100% { transform: scale(0.8); opacity: 0.5; }
        30% { transform: scale(1.2); opacity: 1; }
    }
    
    /* HOLOGRAM EFFECT */
    .hologram {
        position: relative;
        background: linear-gradient(45deg, transparent, rgba(0, 255, 255, 0.1), transparent);
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 15px;
        overflow: hidden;
    }
    
    .hologram::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #0066ff, #00ffff, #ff00ff, #ffff00);
        z-index: -1;
        border-radius: 15px;
        animation: hologram-border 3s linear infinite;
    }
    
    @keyframes hologram-border {
        0% { background-position: 0% 0%; }
        100% { background-position: 400% 400%; }
    }
    
    /* DEMO BANNER */
    .demo-banner {
        background: linear-gradient(45deg, rgba(255, 193, 7, 0.1), rgba(255, 152, 0, 0.1));
        border: 2px solid rgba(255, 193, 7, 0.5);
        border-radius: 15px;
        padding: 15px;
        margin: 20px 0;
        text-align: center;
        animation: demo-glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes demo-glow {
        0% { box-shadow: 0 5px 20px rgba(255, 193, 7, 0.2); }
        100% { box-shadow: 0 8px 30px rgba(255, 193, 7, 0.4); }
    }
</style>
""", unsafe_allow_html=True)

# BANNER DE DEMO
st.markdown("""
<div class="demo-banner">
    <h3 style="color: #ffc107; margin: 0; font-family: 'Orbitron', monospace;">
        🎭 MODO DEMONSTRAÇÃO ATIVO
    </h3>
    <p style="color: #ffca28; margin: 5px 0 0 0; font-family: 'Rajdhani', sans-serif;">
        Esta é uma vitrine visual - Configure suas chaves API para funcionalidade completa
    </p>
</div>
""", unsafe_allow_html=True)

# HEADER ÉPICO COM ANIMAÇÕES
st.markdown("""
<div style="text-align: center; margin-bottom: 40px;">
    <h1>🧠 NEUROCHAT AI</h1>
    <div class="subtitle">
        ⚡ SISTEMA DE BUSCA AVANÇADA ⚡
    </div>
    <div style="margin: 20px 0;">
        <span class="pulse-dot"></span>
        <span class="pulse-dot"></span>
        <span class="pulse-dot"></span>
    </div>
</div>
""", unsafe_allow_html=True)

# Inicializar chatbot em modo demo
if 'chatbot' not in st.session_state:
    with st.spinner("🔄 Inicializando sistema neural..."):
        st.session_state.chatbot = DemoGeminiRAGChatbot()

# LAYOUT PRINCIPAL EM COLUNAS
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    # PAINEL DE CONTROLE PRINCIPAL
    st.markdown("""
    <div class="hologram" style="padding: 25px; margin: 15px 0;">
        <div class="tech-text" style="text-align: center; margin-bottom: 20px;">
            🎯 INTERFACE DE CONSULTA NEURAL
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # FORM FUTURÍSTICO
    with st.form("neural_query_form"):
        st.markdown("### 🔮 **DIGITE SUA PERGUNTA:**")
        
        user_question = st.text_area(
            "",
            placeholder="Ex: Quais são os recursos disponíveis no sistema?",
            value="Como funciona este sistema de IA?",
            height=120,
            help="💡 Digite sua pergunta e veja uma demonstração da interface"
        )
        
        # BOTÃO DE ENVIO ÉPICO
        col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
        with col_btn2:
            submitted = st.form_submit_button("🚀 PROCESSAR CONSULTA", type="primary")

    # PROCESSAMENTO COM EFEITOS VISUAIS
    if submitted and user_question.strip():
        
        # LOADING FUTURÍSTICO
        with st.container():
            st.markdown("""
            <div style="text-align: center; margin: 30px 0;">
                <div class="tech-text">🧠 SISTEMA NEURAL PROCESSANDO...</div>
                <div style="margin: 20px 0;">
                    <span class="pulse-dot"></span>
                    <span class="pulse-dot"></span>
                    <span class="pulse-dot"></span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Barra de progresso futurística
            progress_bar = st.progress(0)
            status_placeholder = st.empty()
            
            # Simular progresso com status tech
            statuses = [
                "🔍 Escaneando base de dados neural...",
                "🧮 Calculando embeddings quânticos...",
                "🔗 Conectando ao índice vetorial...",
                "🤖 IA processando contexto...",
                "✨ Sintetizando resposta..."
            ]
            
            for i, status in enumerate(statuses):
                status_placeholder.markdown(f"<div class='tech-text' style='text-align: center;'>{status}</div>", unsafe_allow_html=True)
                progress_bar.progress((i + 1) * 20)
                time.sleep(0.8)
            
            # EXECUTAR PERGUNTA
            start_time = time.time()
            answer = st.session_state.chatbot.ask_question(user_question)
            processing_time = time.time() - start_time
            
            progress_bar.progress(100)
            status_placeholder.empty()
        
        # RESPOSTA COM DESIGN ÉPICO
        st.markdown("### 🎯 **RESPOSTA DO SISTEMA:**")
        
        st.markdown(f"""
        <div class="response-card">
            <div class="tech-text" style="color: #00ff7f; font-size: 1.4rem; line-height: 1.6;">
                {answer}
            </div>
            <div style="text-align: right; margin-top: 15px; color: #78dbff; font-size: 0.9rem;">
                ⚡ Processado em {processing_time:.2f}s (Demo Mode)
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Salvar no histórico
        if 'history' not in st.session_state:
            st.session_state.history = []
        
        st.session_state.history.append({
            "q": user_question,
            "a": answer,
            "t": processing_time
        })

# SIDEBAR COM ESTATÍSTICAS FUTURÍSTICAS
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h2 style="color: #00ffff; font-family: 'Orbitron', monospace;">
            📊 PAINEL DE CONTROLE
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Informação do modelo
    st.markdown("### 🧠 **MODELO DE IA**")
    st.markdown("**Gemini 2.5 Flash-Lite (Demo)**")
    
    # Estatísticas simuladas
    st.markdown(f"""
    <div class="metric-container">
        <h3 style="color: #00ffff; margin-bottom: 15px;">🧠 DADOS NEURAIS</h3>
        <div style="color: #78dbff; font-size: 1.5rem; font-weight: bold;">
            {st.session_state.chatbot.total_vectors:,}
        </div>
        <div style="color: #78dbff; font-size: 0.9rem;">Vetores Simulados</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-container" style="margin-top: 15px;">
        <h3 style="color: #ff00ff; margin-bottom: 15px;">📐 DIMENSÕES</h3>
        <div style="color: #ff00ff; font-size: 1.5rem; font-weight: bold;">
            {st.session_state.chatbot.dimensions}
        </div>
        <div style="color: #ff00ff; font-size: 0.9rem;">Espaço Vetorial</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Status Demo
    st.markdown("""
    <div class="demo-banner" style="margin-top: 20px;">
        <h4 style="color: #ffc107; margin: 0;">🎭 STATUS</h4>
        <p style="color: #ffca28; margin: 5px 0 0 0; font-size: 0.9rem;">
            Modo Demonstração
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Controles do sistema
    st.markdown("### 🛠️ **CONTROLES**")
    
    if st.button("🗑️ LIMPAR MEMÓRIA", use_container_width=True):
        st.session_state.history = []
        st.rerun()
    
    if st.button("🔄 REINICIAR SISTEMA", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# HISTÓRICO FUTURÍSTICO
if 'history' in st.session_state and st.session_state.history:
    st.markdown("---")
    st.markdown("### 📚 **HISTÓRICO DE CONSULTAS**")
    
    for i, item in enumerate(reversed(st.session_state.history[-3:])):
        with st.expander(f"🔍 Consulta {len(st.session_state.history) - i}: {item['q'][:40]}..."):
            st.markdown(f"**🎯 Pergunta:** {item['q']}")
            st.markdown(f"**🤖 Resposta:** {item['a']}")
            st.markdown(f"**⚡ Tempo:** {item['t']:.2f}s")

# RODAPÉ TECH
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 40px; color: #78dbff; opacity: 0.7;">
    <div class="tech-text">
        🚀 Powered by Honacleon Junior • Google Gemini 2.5 Flash-Lite • Pinecone Vector DB • Streamlit
    </div>
    <div style="margin-top: 10px;">
        <span class="pulse-dot"></span>
        <span class="pulse-dot"></span>
        <span class="pulse-dot"></span>
    </div>
    <div style="margin-top: 15px; font-size: 0.9rem; color: #ffc107;">
        🎭 Esta é uma demonstração visual - Configure chaves API para funcionalidade completa
    </div>
</div>
""", unsafe_allow_html=True)
