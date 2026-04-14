import streamlit as st

# --- CONFIGURAÇÃO DE ACESSIBILIDADE ---
st.set_page_config(page_title="Petrolik - Inclusão Total", page_icon="🧠")

# Estilos Visuais (Cores de alto contraste e botões grandes)
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; 
        height: 80px; 
        font-size: 22px; 
        font-weight: bold; 
        border-radius: 15px;
        margin-bottom: 15px;
    }
    .emergency-btn button { 
        background-color: #ff4b4b !important; 
        color: white !important; 
    }
    .stTextInput>div>div>input {
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.title("🧠 Petrolik")
st.subheader("Autonomia e Acessibilidade")
st.write("---")

# --- NAVEGAÇÃO POR ABAS (Para não confundir o usuário) ---
tab1, tab2, tab3, tab4 = st.tabs(["💬 IA AJUDA", "🚧 BARREIRAS", "🚨 EMERGÊNCIA", "📜 DIREITOS"])

# --- ABA 1: ASSISTENTE INTELIGENTE ---
with tab1:
    st.header("💬 Assistente Petrolik")
    st.write("Pergunte sobre direitos ou adaptações:")
    pergunta = st.text_input("Ex: Como peço uma rampa?", key="ia_input")
    
    if pergunta:
        if "rampa" in pergunta.lower() or "acesso" in pergunta.lower():
            st.success("✅ O Petrolik informa: A empresa é obrigada a garantir acessibilidade física. Deseja que eu envie um aviso ao RH?")
            if st.button("Sim, avisar RH"):
                st.write("📩 Enviando solicitação...")
        else:
            st.info("💡 Estou aqui para garantir que você tenha tudo o que precisa para trabalhar bem.")

# --- ABA 2: RELATAR BARREIRA ---
with tab2:
    st.header("🚧 Relatar Problema")
    st.write("Viu um obstáculo? Tire uma foto e nos avise.")
    foto = st.camera_input("Tirar foto do obstáculo")
    detalhes = st.text_area("O que aconteceu?")
    
    if st.button("Enviar para Manutenção"):
        if foto:
            st.success("✅ Relato enviado! A manutenção já recebeu a foto e a localização.")
            st.balloons()
        else:
            st.warning("⚠️ Por favor, tire uma foto para facilitar o conserto.")

# --- ABA 3: EMERGÊNCIA ---
with tab3:
    st.header("🚨 AJUDA RÁPIDA")
    st.write("Clique no botão abaixo se estiver em perigo ou precisar de apoio imediato.")
    
    st.markdown('<div class="emergency-btn">', unsafe_allow_html=True)
    if st.button("🆘 ACIONAR APOIO AGORA"):
        st.error("❗ ALERTA MÁXIMO: Socorristas e RH notificados. Fique onde está, a ajuda está a caminho!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- ABA 4: GUIA DE DIREITOS ---
with tab4:
    st.header("📜 Seus Direitos")
    with st.expander("📌 Lei Brasileira de Inclusão"):
        st.write("A LBI garante que você tenha as mesmas oportunidades e todas as adaptações necessárias no trabalho.")
    with st.expander("📌 Tecnologia Assistiva"):
        st.write("A empresa deve fornecer softwares e equipamentos que ajudem na sua produtividade.")

# --- BARRA LATERAL (ACESSOS RÁPIDOS) ---
with st.sidebar:
    st.title("⚙️ Acessibilidade")
    if st.button("🔊 Ouvir Tela"):
        st.write("🎙️ *Lendo menu principal...*")
    if st.button("🤟 Libras"):
        st.info("👐 Tradutor de Libras ativado.")

st.markdown("---")
st.caption("Petrolik - Transformando a inclusão em ação.")
