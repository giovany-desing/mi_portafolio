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

def load_dinero_image():
    """Carga la imagen de dinero/ROI"""
    try:
        img_path = "image_dinero.jpg"
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
dinero_image = load_dinero_image()

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
        padding: 4rem 0;
        border-bottom: 1px solid rgba(0,0,0,0.08);
        position: relative;
    }
    
    .hero-title {
        font-size: 5rem;
        line-height: 1;
        margin-bottom: 1.5rem;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #475569;
        font-weight: 300;
        line-height: 1.6;
        max-width: 800px;
        animation: fadeInUp 1s ease-out;
    }
    
    /* --- PROFILE IMAGE CONTAINER --- */
    .profile-image-container {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem;
        min-height: 450px;
    }
    
    .profile-image-wrapper {
        position: relative;
        width: 100%;
        max-width: 380px;
        aspect-ratio: 1;
        border-radius: 50%;
        padding: 8px;
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 50%, #1e3a8a 100%);
        animation: float 6s ease-in-out infinite;
        box-shadow: 0 25px 70px rgba(37, 99, 235, 0.25),
                    0 0 120px rgba(30, 64, 175, 0.15),
                    inset 0 0 30px rgba(37, 99, 235, 0.1);
        transition: all 0.4s ease;
    }
    
    .profile-image-wrapper:hover {
        transform: scale(1.05);
        box-shadow: 0 30px 80px rgba(37, 99, 235, 0.35),
                    0 0 150px rgba(30, 64, 175, 0.2);
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
        content: "";
        position: absolute;
        inset: 0;
        border-radius: 50%;
        padding: 2px;
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.2), rgba(30, 64, 175, 0.2));
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        z-index: 1;
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
        padding: 3rem;
        margin-bottom: 4rem;
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
        margin-bottom: 1rem;
        display: block;
        font-weight: 600;
    }

    /* --- METRICAS DE PROYECTO --- */
    .metric-box {
        border-left: 2px solid #cbd5e1;
        padding-left: 1.5rem;
        margin-top: 2rem;
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
        padding: 1.1rem 3.5rem;
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
    
    /* --- BOTONES "VER INGENIERIA" - AZUL OSCURO DINÁMICO --- */
    .project-card .stButton > button,
    .project-card button[data-testid="baseButton-secondary"],
    div[data-testid="stButton"] > button,
    .project-card a[data-testid="stLinkButton"] > button,
    .project-card .stButton button {
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%) !important;
        background-color: #1e40af !important;
        background-image: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%) !important;
        color: white !important;
        border: none !important;
        border-color: transparent !important;
        padding: 1.2rem 3.5rem !important;
        font-weight: 700 !important;
        border-radius: 16px !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100% !important;
        text-transform: none !important;
        letter-spacing: 0.04em !important;
        font-size: 1.15rem !important;
        position: relative !important;
        overflow: hidden !important;
        box-shadow: 0 12px 35px rgba(30, 64, 175, 0.4),
                    0 6px 18px rgba(30, 58, 138, 0.3),
                    inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
        animation: ingenieriaPulse 2.5s ease-in-out infinite !important;
    }
    
    /* Forzar color azul oscuro en todos los estados */
    .project-card .stButton > button:focus,
    .project-card .stButton > button:visited,
    .project-card .stButton > button:link {
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%) !important;
        background-color: #1e40af !important;
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
            rgba(255, 255, 255, 0.25) 50%, 
            transparent 100%) !important;
        transition: left 0.8s ease !important;
        z-index: 1 !important;
    }
    
    .project-card .stButton > button::after,
    .project-card button[data-testid="baseButton-secondary"]::after {
        content: "" !important;
        position: absolute !important;
        top: 50% !important;
        left: 50% !important;
        width: 0 !important;
        height: 0 !important;
        border-radius: 50% !important;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.3) 0%, transparent 70%) !important;
        transform: translate(-50%, -50%) !important;
        transition: width 0.7s ease, height 0.7s ease !important;
    }
    
    .project-card .stButton > button:hover,
    .project-card button[data-testid="baseButton-secondary"]:hover {
        border: none !important;
        box-shadow: 0 18px 50px rgba(30, 64, 175, 0.6),
                    0 12px 30px rgba(30, 58, 138, 0.5),
                    inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        transform: translateY(-6px) scale(1.03) !important;
        color: white !important;
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%) !important;
        background-color: #1e40af !important;
    }
    
    .project-card .stButton > button:hover::before,
    .project-card button[data-testid="baseButton-secondary"]:hover::before {
        left: 100% !important;
    }
    
    .project-card .stButton > button:hover::after,
    .project-card button[data-testid="baseButton-secondary"]:hover::after {
        width: 350px !important;
        height: 350px !important;
    }
    
    .project-card .stButton > button:active,
    .project-card button[data-testid="baseButton-secondary"]:active {
        transform: translateY(-3px) scale(0.97) !important;
        box-shadow: 0 10px 25px rgba(30, 64, 175, 0.5),
                    0 5px 15px rgba(30, 58, 138, 0.4) !important;
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%) !important;
        background-color: #1e40af !important;
    }
    
    @keyframes ingenieriaPulse {
        0%, 100% {
            box-shadow: 0 12px 35px rgba(30, 64, 175, 0.4),
                        0 6px 18px rgba(30, 58, 138, 0.3);
        }
        50% {
            box-shadow: 0 15px 40px rgba(30, 64, 175, 0.5),
                        0 8px 22px rgba(30, 58, 138, 0.4);
        }
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
        margin: 6rem 0 3rem 0;
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
c1, c2 = st.columns([1.6, 1])

with c1:
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    st.markdown('<div class="status-badge">SENIOR ML ENGINEER & AI ARCHITECT</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">Ingeniería de ML.<br><span class="gradient-text">Nivel Producción.</span></h1>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-subtitle">
        Construyo sistemas inteligentes que resuelven problemas de negocio reales. 
        Desde arquitecturas <b>Multi-Agente con GenAI</b> hasta pipelines de <b>MLOps</b> que se auto-reparan.
        <br><br>
        No busco "probar modelos". <b>Entrego soluciones escalables, seguras y rentables.</b>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Botones de llamada a la acción (CTA)
    col_cta1, col_cta2, col_void = st.columns([1, 1, 1])
    with col_cta1:
        st.link_button("📥 Descargar CV", "TU_LINK_DE_DESCARGA")
    with col_cta2:
        st.link_button("🤝 Agendar Reunión", "mailto:tucorreo@ejemplo.com")
    
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
    <div class="value-card" style="padding: 2.5rem; border-radius: 20px; height: 100%;">
        <div style="margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center; padding: 1rem; background: rgba(37, 99, 235, 0.1); border-radius: 16px; width: fit-content;">
            {icon_html}
        </div>
        <h3 style="font-size: 1.3rem; margin-bottom: 1rem; font-weight: 700; color: #0f172a;">{title}</h3>
        <p style="color: #475569; line-height: 1.7; font-size: 0.95rem;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

with col_v1:
    value_card("🏗️", "Arquitectura Robusta", "No entrego scripts sueltos. Entrego sistemas con **IaC (Terraform)**, Contenedores Dockerizados y orquestación resiliente.", arquitectura_image)
with col_v2:
    value_card("🔄", "MLOps Nativo", "El modelo es solo el 10%. Implemento **DVC, Airflow y Detección de Drift** para garantizar que el sistema no se degrade en producción.", mlops_image)
with col_v3:
    value_card("💰", "Enfoque en ROI", "Cada línea de código está justificada por un impacto en el negocio: reducción de costos, automatización de horas-hombre o mejora en la toma de decisiones.", dinero_image)

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

# --- PROYECTO 3: CHATBOT (La Joya de la Corona) ---
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
            <div style="border-radius: 12px; height: 100%; min-height: 300px; border: 1px solid rgba(0,0,0,0.08); overflow: hidden; background: #ffffff;">
                <img src="data:image/png;base64,{img_str}" alt="Chatbot Architecture" style="width: 100%; height: 100%; object-fit: cover; display: block;">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback si no hay imagen
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%); border-radius: 12px; height: 100%; display: flex; align-items: center; justify-content: center; min-height: 300px; border: 1px solid rgba(0,0,0,0.08);">
                <div style="text-align: center;">
                    <div style="font-size: 4rem;">🤖</div>
                    <div style="margin-top: 1rem; color: #64748b; font-family: 'JetBrains Mono';">System Architecture</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with c_txt:
        st.markdown('<div class="status-badge">GEN AI • CLOUD • MULTI-AGENT</div>', unsafe_allow_html=True)
        st.markdown('<h2>Chatbot Analítico Empresarial con RAG & SQL</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="color: #475569; font-size: 1.1rem; line-height: 1.6;">
            Solución al problema de <b style="color: #0f172a;">"Datos Atrapados"</b>. Transformé bases de datos SQL complejas en una conversación natural. 
            Utilizando una arquitectura de <b style="color: #0f172a;">3 capas de inteligencia</b> (Reglas → Modelo Fine-Tuned → LLM General), 
            este sistema democratiza el acceso a la información sin depender de analistas.
        </p>
        """, unsafe_allow_html=True)
        
        # Métricas de impacto
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric-box"><span class="metric-value">< 2s</span><span class="metric-label">Latencia</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric-box"><span class="metric-value">99.9%</span><span class="metric-label">IaC Terraform</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric-box"><span class="metric-value">100%</span><span class="metric-label">Auto-Scalable</span></div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(render_techs(["LangGraph", "Llama 3.1 Fine-tuned", "AWS RDS/EC2", "Terraform", "PostgreSQL Vector", "Redis"]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botón Premium Central
        st.markdown("""
        <style>
        .ingenieria-btn-container {
            display: flex;
            justify-content: center;
            margin: 2rem 0;
        }
        </style>
        <div class="ingenieria-btn-container">
        """, unsafe_allow_html=True)
        col_btn = st.columns([1, 2, 1])
        with col_btn[1]:
            st.link_button("Ver Ingenieria", "LINK_PROYECTO_CHATBOT", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --- PROYECTO 2: FACTURAS (Automatización Pura) ---
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    c_txt, c_img = st.columns([1.5, 1], gap="large") # Invertimos orden para dinamismo
    
    with c_txt:
        st.markdown('<div class="status-badge">COMPUTER VISION • ETL • AUTOMATION</div>', unsafe_allow_html=True)
        st.markdown('<h2>Sistema de Procesamiento Inteligente de Facturas PDF</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="color: #475569; font-size: 1.1rem; line-height: 1.6;">
            Eliminación total de la intervención humana en cuentas por pagar. 
            Diseñé un pipeline que ingesta PDFs, clasifica con <b style="color: #0f172a;">CNN (Deep Learning)</b> y extrae datos estructurados con <b style="color: #0f172a;">OCR</b>. 
            Lo que tomaba 16 horas al mes, ahora toma segundos.
        </p>
        """, unsafe_allow_html=True)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric-box"><span class="metric-value">0%</span><span class="metric-label">Human Loop</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric-box"><span class="metric-value">95%</span><span class="metric-label">Accuracy CNN</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric-box"><span class="metric-value">Hourly</span><span class="metric-label">ETL Schedule</span></div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(render_techs(["Apache Airflow", "TensorFlow CNN", "Tesseract OCR", "Docker", "AWS S3", "Google Drive API"]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Botón Premium Central
        col_btn = st.columns([1, 2, 1])
        with col_btn[1]:
            st.link_button("Ver Ingenieria", "LINK_PROYECTO_FACTURAS", use_container_width=True)

    with c_img:
        if invoice_image:
            # Convertir imagen a base64 para insertarla en HTML
            buffered = BytesIO()
            invoice_image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            st.markdown(f"""
            <div style="border-radius: 12px; height: 100%; min-height: 300px; border: 1px solid rgba(0,0,0,0.08); overflow: hidden; background: #ffffff;">
                <img src="data:image/jpeg;base64,{img_str}" alt="Invoice Processing System" style="width: 100%; height: 100%; object-fit: cover; display: block;">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback si no hay imagen
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%); border-radius: 12px; height: 100%; display: flex; align-items: center; justify-content: center; min-height: 300px; border: 1px solid rgba(0,0,0,0.08);">
                <div style="text-align: center;">
                    <div style="font-size: 4rem;">📄</div>
                    <div style="margin-top: 1rem; color: #64748b; font-family: 'JetBrains Mono';">Automated Pipeline</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PROYECTO 1: TICKETS (MLOps Puro) ---
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
            <div style="border-radius: 12px; height: 100%; min-height: 300px; border: 1px solid rgba(0,0,0,0.08); overflow: hidden; background: #ffffff;">
                <img src="data:image/png;base64,{img_str}" alt="Ticket Classification System" style="width: 100%; height: 100%; object-fit: cover; display: block;">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback si no hay imagen
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%); border-radius: 12px; height: 100%; display: flex; align-items: center; justify-content: center; min-height: 300px; border: 1px solid rgba(0,0,0,0.08);">
                <div style="text-align: center;">
                    <div style="font-size: 4rem;">🎫</div>
                    <div style="margin-top: 1rem; color: #64748b; font-family: 'JetBrains Mono';">Real-time Classification</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with c_txt:
        st.markdown('<div class="status-badge">MLOPS • FASTAPI • DRIFT DETECTION</div>', unsafe_allow_html=True)
        st.markdown('<h2>Clasificador de Tickets con Ciclo de Vida Auto-Gestionado</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="color: #475569; font-size: 1.1rem; line-height: 1.6;">
            Solución al cuello de botella operativo en Fiduciaria. 
            No es solo un modelo: es un sistema vivo. Detecta <b style="color: #0f172a;">Data Drift</b> automáticamente, 
            dispara reentrenamientos con <b style="color: #0f172a;">Optuna</b> y despliega nuevas versiones sin downtime.
        </p>
        """, unsafe_allow_html=True)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric-box"><span class="metric-value">94%</span><span class="metric-label">F1-Score</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric-box"><span class="metric-value"><1s</span><span class="metric-label">Inferencia</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric-box"><span class="metric-value">Auto</span><span class="metric-label">Retraining</span></div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(render_techs(["FastAPI", "DVC", "XGBoost", "Supabase", "GitHub Actions", "Evidently AI"]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Botón Premium Central
        col_btn = st.columns([1, 2, 1])
        with col_btn[1]:
            st.link_button("Ver Ingenieria", "LINK_PROYECTO_TICKETS", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 7. FOOTER (PERFIL FINAL)
# ==============================================================================
st.markdown('<hr style="border: none; border-top: 1px solid rgba(0,0,0,0.1); margin: 4rem 0;">', unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 4rem 0;">
    <h2 style="font-size: 2.5rem; margin-bottom: 1rem; color: #0f172a;">¿Construimos el futuro?</h2>
    <p style="color: #475569; font-size: 1.2rem; margin-bottom: 2rem;">
        Disponible para liderar iniciativas de IA que requieran arquitectura sólida y visión de negocio.
    </p>
</div>
""", unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns([1, 2, 1])
with col_f2:
    st.link_button("✉️ INICIAR CONVERSACIÓN", "mailto:tucorreo@ejemplo.com", use_container_width=True)

st.markdown("""
<div style="text-align: center; margin-top: 3rem; color: #94a3b8; font-size: 0.8rem;">
    ENGINEERED BY EDGAR YOVANY | 2024
</div>
""", unsafe_allow_html=True)