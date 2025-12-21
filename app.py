import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import os
import base64
from io import BytesIO

# ==============================================================================
# 1. CONFIGURACIÓN DE PÁGINA (MODO FULL WIDE)
# ==============================================================================
st.set_page_config(
    page_title="Edgar Yovany | Lead AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. CARGA DE ASSETS
# ==============================================================================
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200: return None
        return r.json()
    except: return None

def load_profile_image():
    """Carga la imagen de perfil"""
    try:
        img_path = os.path.join("imagenes", "foto.png")
        if os.path.exists(img_path):
            return Image.open(img_path)
        return None
    except:
        return None

def load_chatbot_image():
    """Carga la imagen del chatbot"""
    try:
        img_path = "image_chatbot.png"
        if os.path.exists(img_path):
            return Image.open(img_path)
        return None
    except:
        return None

def load_invoice_image():
    """Carga la imagen de facturas"""
    try:
        img_path = "image_invoice.jpg"
        if os.path.exists(img_path):
            return Image.open(img_path)
        return None
    except:
        return None

def load_tickets_image():
    """Carga la imagen de tickets"""
    try:
        img_path = "image_tickets.png"
        if os.path.exists(img_path):
            return Image.open(img_path)
        return None
    except:
        return None

def load_arquitectura_image():
    """Carga la imagen de arquitectura"""
    try:
        img_path = "image_arquitectura.png"
        if os.path.exists(img_path):
            return Image.open(img_path)
        return None
    except:
        return None

def load_mlops_image():
    """Carga la imagen de MLOps"""
    try:
        img_path = "image_mlops.jpg"
        if os.path.exists(img_path):
            return Image.open(img_path)
        return None
    except:
        return None

def load_robot_image():
    """Carga la imagen de robot/ROI"""
    try:
        img_path = "image_robot.jpg"
        if os.path.exists(img_path):
            return Image.open(img_path)
        return None
    except:
        return None

def load_icfes_image():
    """Carga la imagen del proyecto ICFES"""
    try:
        img_path = "image_regresion.png"
        if os.path.exists(img_path):
            return Image.open(img_path)
        return None
    except:
        return None

# Animación abstracta tecnológica (Red neuronal / Conexiones)
lottie_hero = load_lottieurl("https://lottie.host/6e676082-9602-4632-902e-132d79c65604/7y3K8C5q4F.json")
profile_image = load_profile_image()
chatbot_image = load_chatbot_image()
invoice_image = load_invoice_image()
tickets_image = load_tickets_image()
arquitectura_image = load_arquitectura_image()
mlops_image = load_mlops_image()
robot_image = load_robot_image()
icfes_image = load_icfes_image()

# ==============================================================================
# 3. CSS "ELITE ENGINEERING" (VISUALMENTE IMPACTANTE)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@400;700&display=swap');

    /* --- FONDO Y BASE --- */
    .stApp {
        background-color: #ffffff;
        background-image: radial-gradient(circle at 50% 0%, #f8fafc 0%, #ffffff 60%);
        color: #1e293b;
        font-family: 'Inter', sans-serif;
    }
    
    /* --- REDUCIR ESPACIADO DE COLUMNAS EN HERO --- */
    .hero-container [data-testid="column"] {
        padding: 0.3rem 0.5rem;
    }
    
    /* --- REDUCIR ESPACIADO ESPECÍFICO COLUMNA IMAGEN --- */
    .profile-image-container [data-testid="column"],
    div[data-testid="column"]:has(.profile-image-container) {
        padding: 0.2rem !important;
    }

    /* --- TIPOGRAFÍA DE IMPACTO --- */
    h1, h2, h3 {
        font-weight: 800;
        letter-spacing: -0.04em;
        color: #0f172a;
    }
    
    .gradient-text {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* --- HERO SECTION --- */
    .hero-container {
        padding: 0.5rem 0;
        border-bottom: 1px solid rgba(0,0,0,0.08);
        position: relative;
    }
    
    .hero-title {
        font-size: 4.5rem;
        line-height: 1.1;
        margin-bottom: 0.6rem;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        color: #475569;
        font-weight: 300;
        line-height: 1.5;
        max-width: 800px;
        margin-bottom: 0.3rem;
        animation: fadeInUp 1s ease-out;
    }
    
    /* --- PROFILE IMAGE CONTAINER --- */
    .profile-image-container {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        min-height: auto;
    }
    
    .profile-image-wrapper {
        position: relative;
        width: 100%;
        max-width: 261px;
        aspect-ratio: 1;
        border-radius: 50%;
        padding: 0;
        background: transparent;
        box-shadow: none;
        transition: all 0.4s ease;
        margin: 0 auto;
    }
    
    .profile-image-wrapper:hover {
        transform: scale(1.05);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    .profile-image-inner {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        overflow: hidden;
        background: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
    }
    
    .profile-image-inner::before {
        display: none;
    }
    
    .profile-image-inner img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
        position: relative;
        z-index: 0;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(2deg); }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }

    /* --- TARJETAS DE PROYECTO (ELITE CARDS) --- */
    .project-card {
        background: linear-gradient(135deg, rgba(248, 250, 252, 0.9) 0%, rgba(241, 245, 249, 0.8) 100%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.08);
        border-radius: 24px;
        padding: 2.5rem;
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    }
    
    .project-card::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, transparent, rgba(37, 99, 235, 0.6), rgba(30, 64, 175, 0.6), transparent);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .project-card::after {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(37, 99, 235, 0.05) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.4s ease;
    }

    .project-card:hover {
        transform: translateY(-8px);
        border-color: rgba(37, 99, 235, 0.3);
        box-shadow: 0 25px 50px -12px rgba(37, 99, 235, 0.15),
                    0 0 60px rgba(30, 64, 175, 0.1);
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.9) 100%);
    }
    
    .project-card:hover::before {
        opacity: 1;
    }
    
    .project-card:hover::after {
        opacity: 1;
    }

    /* --- ETIQUETAS Y BADGES --- */
    .tech-pill {
        display: inline-flex;
        align-items: center;
        padding: 6px 16px;
        margin: 0 8px 8px 0;
        background: rgba(241, 245, 249, 0.8);
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 100px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        color: #475569;
        transition: all 0.3s ease;
    }
    
    .tech-pill:hover {
        background: rgba(37, 99, 235, 0.1);
        border-color: #2563eb;
        color: #1e40af;
    }

    .status-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #2563eb;
        margin-bottom: 0.6rem;
        display: block;
        font-weight: 600;
    }

    /* --- METRICAS DE PROYECTO --- */
    .metric-box {
        border-left: 2px solid #cbd5e1;
        padding-left: 1.5rem;
        margin-top: 1.5rem;
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0f172a;
        display: block;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* --- BOTONES DE ACCION PREMIUM --- */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        color: white !important;
        border: none;
        padding: 0.9rem 3.5rem;
        font-weight: 700;
        border-radius: 16px;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        text-transform: none;
        letter-spacing: 0.03em;
        font-size: 1.15rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(37, 99, 235, 0.35),
                    0 5px 15px rgba(37, 99, 235, 0.25),
                    inset 0 1px 0 rgba(255, 255, 255, 0.2);
    }
    
    .stButton > button::before {
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(255, 255, 255, 0.3) 50%, 
            transparent 100%);
        transition: left 0.7s ease;
        z-index: 1;
    }
    
    .stButton > button::after {
        content: "";
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.2);
        transform: translate(-50%, -50%);
        transition: width 0.6s ease, height 0.6s ease;
    }
    
    .stButton > button:hover {
        border: none;
        box-shadow: 0 15px 40px rgba(37, 99, 235, 0.5),
                    0 10px 25px rgba(30, 64, 175, 0.4),
                    inset 0 1px 0 rgba(255, 255, 255, 0.3);
        transform: translateY(-5px) scale(1.02);
        color: white !important;
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover::after {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button:active {
        transform: translateY(-2px) scale(0.98);
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4),
                    0 4px 10px rgba(30, 64, 175, 0.3);
    }
    
    /* Animación de pulso sutil */
    @keyframes premiumPulse {
        0%, 100% {
            box-shadow: 0 10px 30px rgba(37, 99, 235, 0.35),
                        0 5px 15px rgba(37, 99, 235, 0.25);
        }
        50% {
            box-shadow: 0 12px 35px rgba(37, 99, 235, 0.45),
                        0 6px 18px rgba(37, 99, 235, 0.35);
        }
    }
    
    .stButton > button {
        animation: premiumPulse 3s ease-in-out infinite;
    }
    
    /* --- BOTONES "VER INGENIERIA" - AZUL CLARO CON TEXTO BLANCO --- */
    .project-card .stButton > button,
    .project-card button[data-testid="baseButton-secondary"],
    .project-card div[data-testid="stButton"] > button,
    .project-card a[data-testid="stLinkButton"],
    .project-card a[data-testid="stLinkButton"] > button,
    .project-card .stButton button,
    .project-card [data-testid="stLinkButton"] button,
    .ingenieria-btn-container .stButton > button,
    .ingenieria-btn-container a[data-testid="stLinkButton"],
    .ingenieria-btn-container a[data-testid="stLinkButton"] > button,
    .ingenieria-btn-container [data-testid="stLinkButton"] button,
    .ingenieria-btn-container div[data-testid="stButton"] > button {
        background: #3b82f6 !important;
        background-color: #3b82f6 !important;
        background-image: none !important;
        color: white !important;
        border: none !important;
        border-color: transparent !important;
        padding: 0.5rem 1.2rem !important;
        font-weight: 500 !important;
        border-radius: 6px !important;
        transition: all 0.3s ease !important;
        width: auto !important;
        max-width: 180px !important;
        text-transform: none !important;
        letter-spacing: 0.01em !important;
        font-size: 0.85rem !important;
        position: relative !important;
        overflow: hidden !important;
        box-shadow: 0 2px 6px rgba(59, 130, 246, 0.3) !important;
    }
    
    /* Forzar color azul claro en todos los estados */
    .project-card .stButton > button:focus,
    .project-card .stButton > button:visited,
    .project-card .stButton > button:link,
    .project-card a[data-testid="stLinkButton"]:focus,
    .project-card a[data-testid="stLinkButton"]:visited,
    .project-card a[data-testid="stLinkButton"]:link,
    .project-card [data-testid="stLinkButton"] button:focus,
    .project-card [data-testid="stLinkButton"] button:visited,
    .project-card [data-testid="stLinkButton"] button:link,
    .ingenieria-btn-container .stButton > button:focus,
    .ingenieria-btn-container .stButton > button:visited,
    .ingenieria-btn-container .stButton > button:link,
    .ingenieria-btn-container a[data-testid="stLinkButton"]:focus,
    .ingenieria-btn-container a[data-testid="stLinkButton"]:visited,
    .ingenieria-btn-container a[data-testid="stLinkButton"]:link,
    .ingenieria-btn-container [data-testid="stLinkButton"] button:focus,
    .ingenieria-btn-container [data-testid="stLinkButton"] button:visited,
    .ingenieria-btn-container [data-testid="stLinkButton"] button:link {
        background: #3b82f6 !important;
        background-color: #3b82f6 !important;
        color: white !important;
    }
    
    .project-card .stButton > button::before,
    .project-card button[data-testid="baseButton-secondary"]::before {
        content: "" !important;
        position: absolute !important;
        top: 0 !important;
        left: -100% !important;
        width: 100% !important;
        height: 100% !important;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(255, 255, 255, 0.2) 50%, 
            transparent 100%) !important;
        transition: left 0.5s ease !important;
        z-index: 1 !important;
    }
    
    .project-card .stButton > button:hover,
    .project-card button[data-testid="baseButton-secondary"]:hover,
    .project-card a[data-testid="stLinkButton"]:hover,
    .project-card a[data-testid="stLinkButton"]:hover > button,
    .project-card [data-testid="stLinkButton"] button:hover,
    .ingenieria-btn-container .stButton > button:hover,
    .ingenieria-btn-container a[data-testid="stLinkButton"]:hover,
    .ingenieria-btn-container a[data-testid="stLinkButton"]:hover > button,
    .ingenieria-btn-container [data-testid="stLinkButton"] button:hover {
        border: none !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4) !important;
        transform: translateY(-1px) !important;
        color: white !important;
        background: #2563eb !important;
        background-color: #2563eb !important;
    }
    
    .project-card .stButton > button:hover::before,
    .project-card button[data-testid="baseButton-secondary"]:hover::before {
        left: 100% !important;
    }
    
    .project-card .stButton > button:active,
    .project-card button[data-testid="baseButton-secondary"]:active,
    .project-card a[data-testid="stLinkButton"]:active,
    .project-card a[data-testid="stLinkButton"]:active > button,
    .project-card [data-testid="stLinkButton"] button:active,
    .ingenieria-btn-container .stButton > button:active,
    .ingenieria-btn-container a[data-testid="stLinkButton"]:active,
    .ingenieria-btn-container a[data-testid="stLinkButton"]:active > button,
    .ingenieria-btn-container [data-testid="stLinkButton"] button:active {
        transform: translateY(0px) !important;
        box-shadow: 0 1px 4px rgba(59, 130, 246, 0.3) !important;
        background: #3b82f6 !important;
        background-color: #3b82f6 !important;
    }
    
    /* --- BOTÓN PREMIUM CENTRAL --- */
    .premium-button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem 0;
    }

    /* --- SECCIONES --- */
    .section-header {
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        color: #64748b;
        margin: 3rem 0 2rem 0;
        text-align: center;
        position: relative;
        font-weight: 600;
    }
    
    .section-header::before,
    .section-header::after {
        content: "";
        position: absolute;
        top: 50%;
        width: 30%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(37, 99, 235, 0.3), transparent);
    }
    
    .section-header::before {
        left: 0;
    }
    
    .section-header::after {
        right: 0;
    }
    
    /* --- VALUE CARDS --- */
    .value-card {
        background: linear-gradient(135deg, rgba(248, 250, 252, 0.9) 0%, rgba(241, 245, 249, 0.8) 100%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
    
    .value-card:hover {
        transform: translateY(-5px);
        border-color: rgba(37, 99, 235, 0.3);
        box-shadow: 0 15px 35px -10px rgba(37, 99, 235, 0.15);
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.9) 100%);
    }
    
    /* --- SCROLL ANIMATIONS --- */
    @keyframes slideInFromLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInFromRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* --- GLASSMORPHISM EFFECT --- */
    .glass-effect {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. HERO SECTION: "THE PRIZE" - CON FOTO PROFESIONAL
# ==============================================================================
# Layout mejorado: Texto a la izquierda, Foto centrada a la derecha
c1, c2 = st.columns([2.2, 0.8])

with c1:
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)

    st.markdown('<h1 class="hero-title">Ingeniería de ML.<br><span class="gradient-text">Nivel Producción.</span></h1>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-subtitle">
        Soy enfocado en transformar incertidumbre técnica en activos empresariales rentables. No solo despliego modelos, diseño ecosistemas de <b>'Auto-recuperación'</b> y arquitecturas Cloud autónomas que eliminan la deuda técnica y reducen costos operativos. Mi propuesta de valor es clara: construyo sistemas de inteligencia artificial que <b>funcionan solos, reducen costos operativos, automatizan procesos y escalan automáticamente</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="profile-image-container">', unsafe_allow_html=True)
    if profile_image:
        # Convertir imagen a base64 para insertarla en HTML
        buffered = BytesIO()
        profile_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        st.markdown(f"""
        <div class="profile-image-wrapper">
            <div class="profile-image-inner">
                <img src="data:image/png;base64,{img_str}" alt="Edgar Yovany" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Fallback si no hay imagen
        if lottie_hero:
            st_lottie(lottie_hero, height=400, key="hero")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Botones de redes sociales
    st.markdown("""
    <div style="display: flex; flex-direction: row; gap: 0.8rem; margin-top: 1.5rem; align-items: center; justify-content: center;">
        <a href="https://www.linkedin.com/in/edgar-yovany-samaca-acu%C3%B1a-a17452210/" target="_blank" style="text-decoration: none; flex: 1; max-width: 120px;">
            <button style="background: #0f172a; color: white !important; border: none; padding: 0.9rem 1.5rem; font-weight: 700; border-radius: 16px; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); width: 100%; text-transform: none; letter-spacing: 0.03em; font-size: 0.95rem; position: relative; overflow: hidden; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.35), 0 5px 15px rgba(15, 23, 42, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.1); cursor: pointer; font-family: 'Inter', sans-serif;">
                LinkedIn
            </button>
        </a>
        <a href="https://github.com/giovany-desing" target="_blank" style="text-decoration: none; flex: 1; max-width: 120px;">
            <button style="background: #0f172a; color: white !important; border: none; padding: 0.9rem 1.5rem; font-weight: 700; border-radius: 16px; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); width: 100%; text-transform: none; letter-spacing: 0.03em; font-size: 0.95rem; position: relative; overflow: hidden; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.35), 0 5px 15px rgba(15, 23, 42, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.1); cursor: pointer; font-family: 'Inter', sans-serif;">
                GitHub
            </button>
        </a>
    </div>
    <style>
        a[href*="linkedin"] button:hover,
        a[href*="github"] button:hover {
            border: none;
            box-shadow: 0 15px 40px rgba(15, 23, 42, 0.5), 0 10px 25px rgba(15, 23, 42, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2);
            transform: translateY(-5px) scale(1.02);
            color: white !important;
            background: #1e293b;
        }
        a[href*="linkedin"] button:active,
        a[href*="github"] button:active {
            transform: translateY(-2px) scale(0.98);
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.4), 0 4px 10px rgba(15, 23, 42, 0.3);
            background: #0f172a;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 5. FILOSOFÍA DE INGENIERÍA (WHY ME?)
# ==============================================================================
st.markdown('<div class="section-header">MI VALOR DIFERENCIAL</div>', unsafe_allow_html=True)

col_v1, col_v2, col_v3 = st.columns(3, gap="medium")

def value_card(icon, title, desc, image=None):
    if image:
        # Convertir imagen a base64 para insertarla en HTML
        buffered = BytesIO()
        # Detectar el formato de la imagen
        img_format = image.format if image.format else "PNG"
        if img_format == "JPEG":
            image.save(buffered, format="JPEG")
            mime_type = "image/jpeg"
        else:
            image.save(buffered, format="PNG")
            mime_type = "image/png"
        img_str = base64.b64encode(buffered.getvalue()).decode()
        icon_html = f'<img src="data:{mime_type};base64,{img_str}" alt="{title}" style="width: 64px; height: 64px; object-fit: contain; display: block;">'
    else:
        icon_html = f'<div style="font-size: 2.5rem;">{icon}</div>'
    
    st.markdown(f"""
    <div class="value-card" style="padding: 2rem; border-radius: 20px; height: 100%;">
        <div style="margin-bottom: 1.2rem; display: flex; align-items: center; justify-content: center; padding: 1rem; background: rgba(37, 99, 235, 0.1); border-radius: 16px; width: fit-content;">
            {icon_html}
        </div>
        <h3 style="font-size: 1.3rem; margin-bottom: 0.8rem; font-weight: 700; color: #0f172a;">{title}</h3>
        <p style="color: #475569; line-height: 1.7; font-size: 0.95rem;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

with col_v1:
    value_card("🏗️", "Arquitectura \"Cost-First\" (FinOps)", "Tengo la capacidad técnica para alinear la infraestructura Cloud con el estado de resultados de la empresa. Optimizo cada línea de código y recurso en la nube para maximizar el margen de beneficio, logrando que mis soluciones no sean un gasto, sino una inversión autosostenible con un ROI medible en semanas.", arquitectura_image)
with col_v2:
    value_card("🔄", "MLOps \"Zero-Touch\" & Autonomía Operativa", "Mientras otros ingenieros entregan modelos que requieren mantenimiento constante, yo implemento arquitecturas de auto-reparación (drift detection y re-entrenamiento automático). Mis sistemas detectan cuando la data cambia y se adaptan sin intervención humana, garantizando continuidad de negocio 24/7 y liberando al equipo de soporte.", mlops_image)
with col_v3:
    value_card("💰", "Despliego IA generativa en producción", "Supero las implementaciones estándar de LLMs creando sistemas de Inteligencia Híbrida (RAG + LangGraph). Construyo agentes capaces de razonar, corregirse a sí mismos (Self-Correction) y ejecutar acciones complejas sobre bases de datos corporativas con seguridad bancaria, llevando la IA de un \"chat curioso\" a una herramienta de ejecución operativa.", robot_image)

# ==============================================================================
# 6. ARQUITECTURAS DESPLEGADAS (LOS PROYECTOS)
# ==============================================================================
st.markdown('<div class="section-header">ARQUITECTURAS DESPLEGADAS</div>', unsafe_allow_html=True)

# Función para renderizar badgets
def render_techs(tech_list):
    html = ""
    for tech in tech_list:
        html += f'<span class="tech-pill">{tech}</span>'
    return html

# --- PROYECTO 1: PREDICCIÓN PUNTAJE ICFES (ML Predictivo) ---
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    c_txt, c_img = st.columns([1.5, 1], gap="large") # Alternamos con txt-img
    
    with c_txt:
        st.markdown('<div class="status-badge">PROYECTO PERSONAL ‖ NIVEL BASICO</div>', unsafe_allow_html=True)
        st.markdown('<h2>Sistema MLOps de Predicción de Puntaje ICFES</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="color: #475569; font-size: 1.1rem; line-height: 1.6;">
            <b style="color: #0f172a;">Este no es un modelo en un notebook. Es un sistema de Machine Learning en producción real con arquitectura empresarial.</b>
            <br><br>
            Pipeline completamente automatizado de principio a fin: cada actualización del código ejecuta automáticamente el versionado de datos en la nube con DVC + S3, encuentra los mejores parámetros del modelo con Optuna probando 150 configuraciones diferentes, registra todos los experimentos con MLflow, construye la aplicación en un contenedor Docker y la despliega en producción en Render. La API desarrollada en FastAPI carga el modelo al iniciar, valida que los datos de entrada sean correctos y responde predicciones en menos de 100 milisegundos. Trazabilidad completa: cada versión del modelo guarda su identificador único, permitiendo recrear exactamente cualquier versión anterior.
            <br><br>
            <b style="color: #0f172a;">La diferencia:</b> Este proyecto resuelve problemas reales que enfrentan empresas en producción: gestión de datos grandes, experimentación organizada (no prueba y error), despliegue automático sin intervención manual, actualizaciones sin interrumpir el servicio y capacidad de auditar qué modelo está activo en cada momento. Diseñado para escalar horizontalmente según demanda.
            <br><br>
            <b style="color: #0f172a;">Resultado:</b> Modelo con 98.4% de precisión desplegado en la nube, respondiendo predicciones a través de API REST.
        </p>
        """, unsafe_allow_html=True)
        
       
        st.markdown('<div class="metric-box"><span class="metric-value">Stack tecnológico usado</span><span class="metric-label">Software</span></div>', unsafe_allow_html=True)

            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(render_techs(["scikit-learn", "XGBoost", "Optuna", "numpy", "pandas", "MLflow","DVC","AWS S3","FastAPI","Uvicorn","Docker","GitHub Actions","Docker Hub","Git"]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botón Ver Ingenieria
        st.link_button("Ver Ingenieria", "https://icfesapp-f3esput3wngkx3vq2krfph.streamlit.app/", use_container_width=False)

    with c_img:
        if icfes_image:
            # Convertir imagen a base64 para insertarla en HTML
            buffered = BytesIO()
            # Detectar el formato de la imagen
            img_format = icfes_image.format if icfes_image.format else "PNG"
            if img_format == "JPEG":
                icfes_image.save(buffered, format="JPEG")
                mime_type = "image/jpeg"
            else:
                icfes_image.save(buffered, format="PNG")
                mime_type = "image/png"
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            st.markdown(f"""
            <div style="border-radius: 12px; height: 100%; min-height: 210px; border: 1px solid rgba(0,0,0,0.08); overflow: hidden; background: #ffffff; display: flex; align-items: center; justify-content: center;">
                <img src="data:{mime_type};base64,{img_str}" alt="ICFES Prediction Project" style="width: 121%; height: 121%; object-fit: cover; display: block; border-radius: 8px;">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback si no hay imagen
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%); border-radius: 12px; height: 100%; display: flex; align-items: center; justify-content: center; min-height: 210px; border: 1px solid rgba(0,0,0,0.08);">
                <div style="text-align: center;">
                    <div style="font-size: 2.8rem;">📊</div>
                    <div style="margin-top: 0.7rem; color: #64748b; font-family: 'JetBrains Mono';">ML Prediction Model</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PROYECTO 2: TICKETS (MLOps Puro) ---
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    c_img, c_txt = st.columns([1, 1.5], gap="large")
    
    with c_img:
        if tickets_image:
            # Convertir imagen a base64 para insertarla en HTML
            buffered = BytesIO()
            tickets_image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            st.markdown(f"""
            <div style="border-radius: 12px; height: 100%; min-height: 210px; border: 1px solid rgba(0,0,0,0.08); overflow: hidden; background: #ffffff; display: flex; align-items: center; justify-content: center;">
                <img src="data:image/png;base64,{img_str}" alt="Ticket Classification System" style="width: 105%; height: 105%; object-fit: cover; display: block; border-radius: 8px;">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback si no hay imagen
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%); border-radius: 12px; height: 100%; display: flex; align-items: center; justify-content: center; min-height: 210px; border: 1px solid rgba(0,0,0,0.08);">
                <div style="text-align: center;">
                    <div style="font-size: 2.8rem;">🎫</div>
                    <div style="margin-top: 0.7rem; color: #64748b; font-family: 'JetBrains Mono';">Real-time Classification</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with c_txt:
        st.markdown('<div class="status-badge">PROYECTO EMPRESARIAL PARA USO INTERNO ‖ NIVEL INTERMEDIO</div>', unsafe_allow_html=True)
        st.markdown('<h2>Sistema de Clasificación Inteligente de Tickets de Soporte</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="color: #475569; font-size: 1.1rem; line-height: 1.6;">
            Desarrollé un sistema MLOps enterprise-grade end-to-end que automatiza la clasificación de tickets de soporte con <b style="color: #0f172a;">98.35% de precisión</b>, eliminando intervención manual y reduciendo costos operativos en 70-80%. Construí pipeline completo: preprocesamiento NLP en español (NLTK tokenización + stemming Snowball + TF-IDF 5000D) → entrenamiento de 7 algoritmos optimizados con Optuna (búsqueda bayesiana 20 trials × 3-fold CV) → deployment continuo con auto-recuperación.
            <br><br>
            Implementé <b style="color: #0f172a;">FastAPI</b> por su arquitectura asíncrona ASGI (30 req/min, &lt;500ms latencia), validación Pydantic automática, y <b style="color: #0f172a;">hot-reload de modelos sin downtime</b> — crítico para actualizar en producción sin afectar SLAs. Desplegué <b style="color: #0f172a;">Apache Airflow</b> para orquestación on-premise con DAGs visuales, retry logic granular, y ShortCircuitOperators que previenen reentrenamientos innecesarios, reduciendo costos computacionales 60%.
            <br><br>
            Optimicé entrenamiento comparando Gradient Boosting vs XGBoost vs LightGBM, seleccionando objetivamente el mejor. Versioné con DVC + S3 (datasets y modelos), Hice tracking de experimentos con MLflow (params, metrics, artifacts). Construí drift detection tri-dimensional (KS-test, Chi-square, vocabulary growth) que detecta degradación en &lt;6 horas y dispara auto-retrain solo si mejora ≥1%.
            <br><br>
            Desplegué dual orchestration (GitHub Actions cloud + Airflow on-premise) para máxima flexibilidad. Implementé procesamiento batch (100 tickets simultáneos via vectorización NumPy), reduciendo migraciones 97% (5,000 tickets en 5 min vs 3h). El sistema se <b style="color: #0f172a;">auto-mantiene</b>: detecta drift de vocabulario ("Teams", "Zoom" nuevos) → retrain con datos actualizados → valida mejora → hot-reload API → notifica — <b style="color: #0f172a;">cero intervención humana</b>.
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="metric-box"><span class="metric-value">Stack tecnológico usado</span><span class="metric-label">Software</span></div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(render_techs(["Python 3.9", "FastAPI", "scikit-learn", "XGBoost", "LightGBM", "Optuna", "NLTK", "DVC", "MLflow", "Airflow", "GitHub Actions", "Postgresql Supabase", "AWS S3", "Render", "pytest"]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botón Ver Ingenieria
        st.link_button("Ver Ingenieria", "https://fiduciaticketapprterapp-825d6duggvtwzndc65qx4r.streamlit.app/", use_container_width=False)

    st.markdown('</div>', unsafe_allow_html=True)

# --- PROYECTO 3: FACTURAS (Automatización Pura) ---
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    c_txt, c_img = st.columns([1.5, 1], gap="large") # Invertimos orden para dinamismo
    
    with c_txt:
        st.markdown('<div class="status-badge">PROYECTO PARA USO EMPRESARIAL ‖ NIVEL AVANZADO PLUS</div>', unsafe_allow_html=True)
        st.markdown('<h2>Sistema ETL de Facturas con Machine Learning</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="color: #475569; font-size: 1.1rem; line-height: 1.6;">
            Diseñé y construí un sistema inteligente que automatiza el procesamiento de facturas textiles usando inteligencia artificial, reduciendo tiempo de clasificación manual de horas a segundos.
            <br><br>
            El sistema analiza cada factura, la clasifica automáticamente de acuerdo a reglas de negocio establecidas por el cliente, extrae información clave y la organiza en bases de datos para análisis de negocio. Todo desplegado en la nube con AWS usando arquitectura serverless, escalando automáticamente según la demanda.
            <br><br>
            <b style="color: #0f172a;">Impacto:</b>
            <br>
            - ⚡ <b>Velocidad:</b> De horas de clasificación manual a procesamiento en segundos
            <br>
            - 🎯 <b>Precisión:</b> >90% accuracy vs errores humanos variables
            <br>
            - 📈 <b>Escalabilidad:</b> Maneja picos de demanda automáticamente
            <br>
            - 💰 <b>Costo:</b> Solo pagas por lo que usas (modelo serverless)
            <br>
            - 🔄 <b>Mejora Continua:</b> El modelo se reentrena automáticamente cuando detecta cambios en los patrones de datos
            <br><br>
            <b style="color: #0f172a;">Valor Técnico</b>
            <br><br>
            Este proyecto refleja mi capacidad para:
            <br><br>
            1. Diseñar soluciones escalables considerando trade-offs (costo, complejidad, mantenibilidad)
            <br>
            2. Implementar ML en producción no solo entrenar modelos, sino todo el lifecycle
            <br>
            3. Usar Infrastructure as Code para sistemas reproducibles y mantenibles
            <br>
            4. Automatizar desde el código hasta el deployment (true DevOps/MLOps)
            <br>
            5. Documentar profesionalmente para sostenibilidad a largo plazo
            <br><br>
            <b style="color: #0f172a;">No es solo un proyecto de Machine Learning—es una solución empresarial completa que podría ponerse en producción hoy.</b>
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="metric-box"><span class="metric-value">Stack tecnológico usado</span><span class="metric-label">Software</span></div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(render_techs(["Python", "FastAPI", "TensorFlow", "Apache Airflow", "Docker", "Terraform", "MySQL", "Pytesseract","MLflow","DVC","Google Drive API","Git","AWS Services"]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botón Ver Ingenieria
        st.link_button("Ver Ingenieria", "https://clasificador-facturas-app-exkjbpacjtyensqtkxhtmo.streamlit.app/", use_container_width=False)

    with c_img:
        if invoice_image:
            # Convertir imagen a base64 para insertarla en HTML
            buffered = BytesIO()
            invoice_image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            st.markdown(f"""
            <div style="border-radius: 12px; height: 100%; min-height: 210px; border: 1px solid rgba(0,0,0,0.08); overflow: hidden; background: #ffffff; display: flex; align-items: center; justify-content: center;">
                <img src="data:image/jpeg;base64,{img_str}" alt="Invoice Processing System" style="width: 105%; height: 105%; object-fit: cover; display: block; border-radius: 8px;">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback si no hay imagen
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%); border-radius: 12px; height: 100%; display: flex; align-items: center; justify-content: center; min-height: 210px; border: 1px solid rgba(0,0,0,0.08);">
                <div style="text-align: center;">
                    <div style="font-size: 2.8rem;">📄</div>
                    <div style="margin-top: 0.7rem; color: #64748b; font-family: 'JetBrains Mono';">Automated Pipeline</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PROYECTO 4: CHATBOT (La Joya de la Corona) ---
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    c_img, c_txt = st.columns([1, 1.5], gap="large")
    
    with c_img:
        if chatbot_image:
            # Convertir imagen a base64 para insertarla en HTML
            buffered = BytesIO()
            chatbot_image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            st.markdown(f"""
            <div style="border-radius: 12px; height: 100%; min-height: 210px; border: 1px solid rgba(0,0,0,0.08); overflow: hidden; background: #ffffff; display: flex; align-items: center; justify-content: center;">
                <img src="data:image/png;base64,{img_str}" alt="Chatbot Architecture" style="width: 113%; height: 113%; object-fit: cover; display: block; border-radius: 8px;">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback si no hay imagen
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%); border-radius: 12px; height: 100%; display: flex; align-items: center; justify-content: center; min-height: 210px; border: 1px solid rgba(0,0,0,0.08);">
                <div style="text-align: center;">
                    <div style="font-size: 2.8rem;">🤖</div>
                    <div style="margin-top: 0.7rem; color: #64748b; font-family: 'JetBrains Mono';">System Architecture</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with c_txt:
        st.markdown('<div class="status-badge">PROYECTO PARA USO EMPRESARIAL ‖ NIVEL AVANZADO</div>', unsafe_allow_html=True)
        st.markdown('<h2>Chatbot Analítico Empresarial</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="color: #475569; font-size: 1.1rem; line-height: 1.6;">
            Desarrollé un <b style="color: #0f172a;">sistema de BI conversacional</b> que elimina la barrera técnica entre usuarios de negocio y sus datos. El problema: analistas y gerentes dependen de equipos técnicos para consultas SQL básicas, con tiempos de respuesta de días. Mi solución: un chatbot que transforma preguntas en español natural a SQL optimizado, visualizaciones profesionales y KPIs calculados, <b style="color: #0f172a;">todo en menos de 2 segundos.</b>
            <br><br>
            La arquitectura implementa un <b style="color: #0f172a;">pipeline de inteligencia en 3 capas</b> (reglas determinísticas → modelo GPT fine-tuned → Llama 3.3 70B) que optimiza costo-precisión automáticamente. El núcleo es un <b style="color: #0f172a;">grafo de estados con LangGraph</b> que orquesta flujos adaptativos con <b style="color: #0f172a;">RAG semántico</b> sobre pgvector para few-shot learning. Implementé self-correction automática mediante análisis de errores SQL, logrando <b style="color: #0f172a;">96% de accuracy</b> en generación de queries.
            <br><br>
            Infraestructura full IaC con Terraform en AWS (VPC, RDS, EC2, S3), <b style="color: #0f172a;">CI/CD completo</b>, y un <b style="color: #0f172a;">feedback loop cerrado</b> que triggerea reentrenamiento automático cuando las métricas caen bajo umbral. Performance tracker con observabilidad granular: percentiles P50/P95/P99, error classification, y métricas de confianza del modelo.
            <br><br>
            <b style="color: #0f172a;">Resultados:</b> ~$38/mes para 10k queries, 1.2s latencia media, 45% cache hit rate, deployed con auto-scaling y disaster recovery.
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="metric-box"><span class="metric-value">Stack tecnológico usado</span><span class="metric-label">Software</span></div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(render_techs(["FastAPI", "LangChain", "LangGraph", "Llama 3.1 8B (Fine-tuned)","GPT-3.5 (Fine-tuned)", "sentence-transformers", "PostgreSQL + pgvector", "MySQL (AWS RDS)", "Plotly", "Pandas", "NumPy", "EC2 (t3.micro)", "AWS","S3", "CloudWatch", "Docker", "Docker Compose", "Terraform", "GitHub Actions", "pytest"]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botón Ver Ingenieria
        st.link_button("Ver Ingenieria", "https://chatbotapp-tqbqjw97ruumscgjf5km49.streamlit.app/", use_container_width=False)

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 7. FOOTER (PERFIL FINAL)
# ==============================================================================
st.markdown('<hr style="border: none; border-top: 1px solid rgba(0,0,0,0.1); margin: 2.5rem 0;">', unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 2.5rem 0;">
    <h2 style="font-size: 2.5rem; margin-bottom: 1rem; color: #0f172a;">¿Construimos el futuro?</h2>
    <p style="color: #475569; font-size: 1.2rem; margin-bottom: 1.5rem;">
        Disponible para liderar iniciativas de IA que requieran arquitectura sólida y visión de negocio.
    </p>
</div>
""", unsafe_allow_html=True)


