import streamlit as st
from streamlit_lottie import st_lottie
import requests

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Portafolio ML Engineer | [Tu Nombre]",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CARGADOR DE LOTTIE ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ai = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_m9zragkd.json") # Animación Neural Network

# --- CSS PREMIUM (GLASSMORPHISM & GLOW) ---
st.markdown("""
    <style>
    /* Importar fuente Inter */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #FFFFFF;
        color: #4A5568;
    }

    /* Fondo oscuro solo en el área principal */
    div[data-testid="stAppViewContainer"] > div:first-child {
        background-color: #0E1117;
    }

    main[data-testid="stMain"] {
        background-color: #0E1117;
    }

    /* Títulos con gradiente */
    .gradient-text {
        background: linear-gradient(90deg, #3B82F6 0%, #60A5FA 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3.5rem;
        line-height: 1.1;
    }

    .sub-gradient {
        background: linear-gradient(90deg, #64748B 0%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
        font-size: 1.5rem;
    }

    /* Efecto Glassmorphism para las tarjetas */
    div[data-testid="stContainer"] {
        background: #FFFFFF;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        padding: 2rem;
        box-shadow: 0 4px 16px 0 rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    div[data-testid="stContainer"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px 0 rgba(59, 130, 246, 0.15);
        border: 1px solid rgba(59, 130, 246, 0.3);
    }

    /* Botones personalizados */
    .stButton>button {
        background: linear-gradient(92.88deg, #64748B 9.16%, #3B82F6 43.89%, #2563EB 64.72%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        box-shadow: 0 5px 15px rgba(59, 130, 246, 0.3);
        transform: scale(1.02);
        background: linear-gradient(92.88deg, #475569 9.16%, #2563EB 43.89%, #1D4ED8 64.72%);
    }

    /* Badges de tecnología */
    .tech-pill {
        display: inline-flex;
        align-items: center;
        padding: 6px 14px;
        margin: 4px;
        border-radius: 50px;
        background: #F1F5F9;
        border: 1px solid #CBD5E1;
        font-size: 0.8rem;
        color: #475569;
        transition: 0.2s;
    }
    .tech-pill:hover {
        background: #E0E7FF;
        border-color: #3B82F6;
        color: #2563EB;
        cursor: default;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E2E8F0;
    }
    
    /* Ajustar colores de texto en markdown */
    .stMarkdown {
        color: #4A5568;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #1E293B;
    }

    /* Colores claros para el área principal con fondo oscuro */
    main[data-testid="stMain"] .stMarkdown,
    main[data-testid="stMain"] p,
    main[data-testid="stMain"] div {
        color: #E2E8F0;
    }

    main[data-testid="stMain"] h1,
    main[data-testid="stMain"] h2,
    main[data-testid="stMain"] h3,
    main[data-testid="stMain"] h4,
    main[data-testid="stMain"] h5,
    main[data-testid="stMain"] h6 {
        color: #FAFAFA;
    }
    
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR (TU PERFIL PERSISTENTE) ---
with st.sidebar:
    # Cargar tu foto de perfil (coloca tu imagen en la carpeta del proyecto)
    # Puedes usar: "foto_perfil.jpg", "foto_perfil.png", etc.
    try:
        st.image("foto_perfil.jpg", width=150, use_container_width=False)
    except:
        # Si no encuentra la imagen, no muestra nada
        pass 
    st.markdown("## Yovany Samaca Acuña")
    st.markdown('<p class="sub-gradient">Senior ML Engineer</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    **📍 Ubicación:** Colombia  
    **📧 Email:** egsamaca56@gmail.com  
    **📱 Teléfono:** [+57 3016953459]
    """)
    
    st.markdown("---")
    st.markdown("### ⚡ Stack Rápido")
    st.markdown("""
    - 🐍 Python & SQL
    - 🏗️ AWS / Render / Docker
    - ⚙️ Airflow & DVC
    - 🤖 PyTorch & LangChain
    """)
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center;">
        <a href="TU_LINKEDIN" target="_blank" style="text-decoration: none; font-size: 24px; margin-right: 15px;">🔗</a>
        <a href="TU_GITHUB" target="_blank" style="text-decoration: none; font-size: 24px;">🐙</a>
    </div>
    """, unsafe_allow_html=True)


# --- MAIN CONTENT ---

# HERO SECTION
col_text, col_anim = st.columns([1.5, 1], gap="medium")

with col_text:
    st.markdown('<h1 class="gradient-text">Arquitectura de ML.<br>Escalabilidad.<br>Resultados.</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 1.2rem; color: #B0B3B8; margin-top: 20px; line-height: 1.6;">
    No solo construyo modelos, construyo <b>sistemas resilientes</b>. <br>
    Ayudo a empresas a transformar experimentos de Data Science en 
    soluciones de producción <b>automatizadas, monitoreadas y rentables</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Spacer
    c1, c2 = st.columns([1, 1])
    with c1:
        st.button("📥 Descargar CV") # Enlaza esto a tu PDF si puedes
    with c2:
        st.link_button("✉️ Contactar Ahora", "mailto:tucorreo@email.com")

with col_anim:
    try:
        st.image("imagenes/foto.png", use_container_width=True)
    except:
        # Si no encuentra la imagen, muestra un mensaje
        st.info("Imagen no encontrada")

st.write("---")

# --- VALUE PROPOSITION (EL FACTOR "WOW") ---
st.markdown('<h2 style="text-align: center; margin-bottom: 2rem; color: #FAFAFA;">💡 ¿Por qué mi perfil es diferente?</h2>', unsafe_allow_html=True)

vp1, vp2, vp3 = st.columns(3, gap="medium")

with vp1:
    with st.container():
        st.markdown("### 🔄 MLOps Nativo")
        st.markdown("El modelo es solo el 20%. El resto es **Infraestructura**. Diseño pipelines CI/CD que detectan Data Drift y reentrenan automáticamente.")

with vp2:
    with st.container():
        st.markdown("### 🏗️ End-to-End Engineering")
        st.markdown("Desde la ETL cruda hasta la API en FastAPI de alta concurrencia. **Testing, Logging, Dockerización** y Despliegue en Nube.")

with vp3:
    with st.container():
        st.markdown("### 💰 Impacto de Negocio")
        st.markdown("Hablo el idioma de los stakeholders. Mis sistemas están diseñados para maximizar el **ROI** y reducir la carga operativa manual.")

st.write("---")

# --- PROYECTOS (LA JOYA DE LA CORONA) ---
st.markdown('<h2 class="gradient-text" style="font-size: 2.5rem;">🚀 Proyectos Desplegados</h2>', unsafe_allow_html=True)
st.markdown("Cada proyecto es una aplicación web en vivo con arquitectura documentada.")

# Función auxiliar para Badges
def tech_badges(tech_list):
    html = ""
    for tech in tech_list:
        html += f'<span class="tech-pill">{tech}</span>'
    return html

# --- PROYECTO 4 ---
with st.container():
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.markdown("### 🤖 Chatbot Analítico 'Agentic' (RAG + SQL)")
        st.markdown("**El Reto:** Los gerentes necesitaban KPIs instantáneos sin depender del equipo de BI.")
        st.markdown("**La Solución:** Un agente autónomo construido con **LangGraph** que consulta MySQL en tiempo real, genera gráficas y aprende del feedback del usuario.")
        st.markdown(tech_badges(["GenAI", "LangChain", "MySQL", "RAG", "Streamlit"]), unsafe_allow_html=True)
        st.write("")
        if st.button("Ver Ingeniería ➡️", key="p4"):
            st.markdown(f'<meta http-equiv="refresh" content="0;url=LINK_PROYECTO_4">', unsafe_allow_html=True)
            
    with c2:
        # Aquí podrías poner un screenshot pequeño si quisieras, o dejar el texto respirar
        st.info("💡 **Feature Estrella:** Sistema de Feedback Loop que reentrena/afina el prompt basado en la satisfacción del usuario.")

st.write("") 

# --- PROYECTO 3 ---
with st.container():
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.markdown("### 📄 Clasificación de Facturas & OCR (ETL + Airflow)")
        st.markdown("**El Reto:** 1000+ horas hombre perdidas digitando facturas manualmente.")
        st.markdown("**La Solución:** Pipeline orquestado en **Airflow**. OCR extrae datos, ML clasifica el segmento y ETL guarda en Drive + SQL. Reentrenamiento 100% automático.")
        st.markdown(tech_badges(["Apache Airflow", "OCR Tesseract", "DVC", "Docker", "MySQL"]), unsafe_allow_html=True)
        st.write("")
        if st.button("Ver Ingeniería ➡️", key="p3"):
            st.markdown(f'<meta http-equiv="refresh" content="0;url=LINK_PROYECTO_3">', unsafe_allow_html=True)
            
    with c2:
        st.success("⚡ **Arquitectura:** ETL programada cada hora con monitoreo de salud cada 3 días.")

st.write("")

# --- PROYECTO 2 ---
with st.container():
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.markdown("### 🎫 Clasificador Inteligente de Tickets IT")
        st.markdown("**El Reto:** Cuellos de botella en Mesa de Ayuda por triaje manual.")
        st.markdown("**La Solución:** API en FastAPI con monitoreo de **Data Drift**. Si la distribución de datos cambia, el sistema dispara un workflow de Github Actions para reentrenar.")
        st.markdown(tech_badges(["FastAPI", "GitHub Actions", "Drift Detection", "Supabase", "Pydantic"]), unsafe_allow_html=True)
        st.write("")
        if st.button("Ver Ingeniería ➡️", key="p2"):
             st.markdown(f'<meta http-equiv="refresh" content="0;url=LINK_PROYECTO_2">', unsafe_allow_html=True)

    with c2:
        st.warning("🛡️ **Robustez:** Implementación de tests unitarios y validación de esquemas con Pydantic.")

st.write("")

# --- PROYECTO 1 ---
with st.container():
    st.markdown("### 🎓 Predicción Académica (ICFES)")
    st.markdown("Despliegue de modelo clásico optimizado para latencia mínima usando **FastAPI** y Render.com. Demo en vivo de buenas prácticas de código.")
    st.markdown(tech_badges(["Scikit-Learn", "Rest API", "Clean Architecture"]), unsafe_allow_html=True)
    if st.button("Ver Ingeniería ➡️", key="p1"):
         st.markdown(f'<meta http-equiv="refresh" content="0;url=LINK_PROYECTO_1">', unsafe_allow_html=True)

st.write("---")

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <h3 class="gradient-text" style="font-size: 2rem;">¿Listo para escalar el equipo de datos?</h3>
    <p style="color: #B0B3B8;">Estoy disponible para entrevistas y pruebas técnicas.</p>
</div>
""", unsafe_allow_html=True)