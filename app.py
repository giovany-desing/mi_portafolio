import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Edgar - Portafolio",
    page_icon="👨‍💻",
    layout="wide"
)

# CSS personalizado para un diseño impactante
st.markdown("""
<style>
    /* 1. Fondo principal de la aplicación: BLANCO */
    .stApp {
        background-color: #ffffff; /* Blanco puro */
    }
    
    /* Eliminar animación de fondo ya que no es necesaria en fondo blanco */
    @keyframes gradient {
        /* No se usa */
    }
    
    /* 2. Contenedor principal con efecto glassmorphism */
    /* Mantenemos el efecto Glassmorphism, ajustando la sombra y el borde para blanco */
    .main .block-container {
        background: rgba(255, 255, 255, 0.7); /* Ligeramente transparente sobre blanco */
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1); /* Sombra más oscura para fondo claro */
        border: 1px solid rgba(0, 0, 0, 0.1); /* Borde suave */
    }
    
    /* 3. Header con efecto de brillo (AJUSTADO para fondo claro) */
    .main-header {
        font-size: 4rem;
        font-weight: 900;
        /* Nuevo gradiente de texto para fondo blanco: tonos azules */
        background: linear-gradient(45deg, #00308F, #007FFF, #00308F); 
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: shine 3s linear infinite;
        text-shadow: 0 0 10px rgba(0,0,0,0.2); /* Sombra oscura sutil */
    }
    
    @keyframes shine {
        to { background-position: 200% center; }
    }
    
    .subheader {
        font-size: 2rem;
        color: #333333; /* Color oscuro para contraste en fondo blanco */
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
        text-shadow: none; /* Quitamos la sombra de texto innecesaria */
    }
    
    /* 4. Imagen de perfil circular con efecto hover (se mantiene) */
    .profile-container {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
    
    .profile-image {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        border: 5px solid rgba(0,0,0,0.1); /* Borde sutil */
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        object-fit: cover;
    }
    
    .profile-image:hover {
        transform: scale(1.1) rotate(5deg);
        box-shadow: 0 15px 60px rgba(0,0,0,0.2);
    }
    
    /* 5. Tarjetas de contacto con efecto glass (AJUSTADO) */
    .contact-info {
        background: rgba(255, 255, 255, 0.8); /* Fondo casi blanco */
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .contact-info:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    
    .contact-info h4 {
        color: #007FFF; /* Título de contacto azul brillante */
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }
    
    .contact-info p, .contact-info a {
        color: #333333; /* Texto oscuro */
        text-decoration: none;
        font-size: 1rem;
    }
    
    .contact-info a:hover {
        color: #00308F; /* Azul más oscuro al pasar el cursor */
        text-decoration: underline;
    }
    
    /* 6. Secciones con fondo semi-transparente (AJUSTADO) */
    .section-container {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        border: 1px solid rgba(0, 0, 0, 0.1);
    }
    
    /* 7. Headers de sección (AJUSTADO) */
    h1, h2, h3 {
        color: #00308F !important; /* Azul oscuro para headers */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    /* 8. Texto general (AJUSTADO) */
    p, li, div:not(.stApp) {
        color: #333333 !important; /* Texto oscuro */
    }
    
    /* 9. Tarjetas de proyecto con efecto 3D (AJUSTADO) */
    .project-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        border: 1px solid rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .project-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        /* Brillo sutil para fondo claro */
        background: linear-gradient(45deg, transparent, rgba(0,0,0,0.05), transparent); 
        transform: rotate(45deg);
        transition: all 0.5s;
    }
    
    .project-card:hover::before {
        left: 100%;
    }
    
    .project-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    }
    
    .project-title {
        font-size: 1.8rem;
        color: #007FFF; /* Título azul */
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    .project-description {
        color: #333333; /* Texto oscuro */
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    
    .project-tech {
        background: rgba(0, 127, 255, 0.1); /* Fondo claro de tecnología */
        padding: 0.8rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: #00308F; /* Texto azul oscuro */
        font-family: 'Courier New', monospace;
    }
    
    /* 10. Botón (AJUSTADO) */
    .project-button {
        display: inline-block;
        background: linear-gradient(45deg, #007FFF, #00308F); /* Gradiente azul fuerte */
        color: white;
        padding: 12px 30px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 127, 255, 0.4);
        margin-top: 1rem;
    }
    
    .project-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0, 127, 255, 0.6);
        background: linear-gradient(45deg, #00308F, #007FFF);
    }
    
    /* 11. Divider con gradiente (AJUSTADO) */
    .divider {
        border: none;
        height: 2px;
        /* Gradiente sutil para fondo claro */
        background: linear-gradient(90deg, transparent, rgba(0,0,0,0.2), transparent); 
        margin: 3rem 0;
    }
    
    /* 12. Tablas con estilo mejorado (AJUSTADO) */
    table {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        overflow: hidden;
    }
    
    th {
        background: rgba(0, 127, 255, 0.3) !important; /* Fondo de encabezado de tabla azul claro */
        color: #00308F !important; /* Texto oscuro */
    }
    
    td {
        color: #333333 !important; /* Texto oscuro */
        border-color: rgba(0, 0, 0, 0.1) !important;
    }
    
    /* 13. Expander personalizado (AJUSTADO) */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        color: #00308F !important; /* Texto azul oscuro */
    }
    
    /* 14. Footer (AJUSTADO) */
    .footer {
        text-align: center;
        color: #333333; /* Texto oscuro */
        margin-top: 3rem;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

# Header principal con imagen de perfil
st.markdown('<div class="main-header">Edgar Yovany Samaca Acuña</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Cientifico de datos</div>', unsafe_allow_html=True)

# Imagen de perfil
# IMPORTANTE: Reemplaza la URL con la URL de tu imagen de perfil
# Puedes subirla a imgur.com, postimages.org o usar una URL directa
st.markdown("""
<div class="profile-container">
    <img src="https://via.placeholder.com/200" class="profile-image" alt="Edgar Mirringa">
</div>
""", unsafe_allow_html=True)

# Descripción breve
st.markdown("""
<div style='text-align: center; font-size: 1.2rem; color: #fff; margin: 2rem 0;'>
<strong>Profesional apasionado por los datos y la tecnología.</strong><br>
Especializado en transformar datos en insights accionables y crear soluciones innovadoras.
</div>
""", unsafe_allow_html=True)

# Información de contacto en columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="contact-info">
        <h4>📧 Contacto</h4>
        <p>egsamaca56@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-info">
        <h4>🔗 LinkedIn</h4>
        <p><a href="https://www.linkedin.com/in/edgar-yovany-samaca-acu%C3%B1a-a17452210/" target="_blank">Conectemos</a></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="contact-info">
        <h4>💻 GitHub</h4>
        <p><a href="https://github.com/giovany-desing" target="_blank">Mi perfil</a></p>
    </div>
    """, unsafe_allow_html=True)

# Divider
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Sección Sobre Mí
st.header("👨‍💻 Sobre Mí")
st.write("""
Profesional con experiencia en análisis de datos, machine learning y desarrollo de aplicaciones.
Mi pasión es resolver problemas complejos utilizando tecnología de vanguardia.

**Destacados:**
- 🎓 Experiencia en análisis de datos y visualización
- 🤖 Desarrollo de modelos de Machine Learning
- 📊 Creación de dashboards interactivos
- 🚀 Siempre explorando nuevas tecnologías
""")

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Sección Habilidades Técnicas
st.header("🛠️ Habilidades Técnicas")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("💻 Lenguajes")
    st.write("""
    - Python 🐍

    - SQL 🗄️

    """)

with col2:
    st.subheader("🚀 Frameworks")
    st.write("""
    - Streamlit
    - Pandas & NumPy
    - Scikit-learn
    - TensorFlow
    - FastAPI
    """)

with col3:
    st.subheader("🔧 Herramientas")
    st.write("""
    - Git & GitHub
    - Docker
    - Jupyter
    - Power BI
    - AWS
    """)

with col4:
    st.subheader("🔧 Herramientas")
    st.write("""
    - Git & GitHub
    - Docker
    - Jupyter
    - Power BI
    - AWS
    """)





st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Sección de proyectos destacados
st.header("🚀 Proyectos Destacados")

# Proyecto 1
st.markdown("""
<div class="project-card">
    <div class="project-title">📊 Dashboard Analítico Avanzado</div>
    <div class="project-description">
        Plataforma interactiva para visualización y análisis de datos en tiempo real. 
        Incluye gráficos dinámicos, filtros avanzados y exportación de reportes.
    </div>
    <div class="project-tech">
        <strong>Tecnologías:</strong> Python, Streamlit, Pandas, Plotly, PostgreSQL
    </div>
    <a href="https://github.com/tu-usuario/proyecto1" target="_blank" class="project-button">
        🔗 Ver Proyecto en GitHub
    </a>
    <a href="https://tu-app-dashboard.streamlit.app" target="_blank" class="project-button" style="margin-left: 10px;">
        🌐 Demo en Vivo
    </a>
</div>
""", unsafe_allow_html=True)

# Proyecto 2
st.markdown("""
<div class="project-card">
    <div class="project-title">🤖 Sistema de Predicción con ML</div>
    <div class="project-description">
        Modelo de machine learning para predicción de tendencias. Incluye preprocesamiento 
        de datos, entrenamiento de modelos y API para integración.
    </div>
    <div class="project-tech">
        <strong>Tecnologías:</strong> Python, Scikit-learn, FastAPI, Docker, AWS
    </div>
    <a href="https://github.com/tu-usuario/proyecto2" target="_blank" class="project-button">
        🔗 Ver Proyecto en GitHub
    </a>
    <a href="https://tu-ml-app.herokuapp.com" target="_blank" class="project-button" style="margin-left: 10px;">
        🌐 Demo en Vivo
    </a>
</div>
""", unsafe_allow_html=True)

# Proyecto 3
st.markdown("""
<div class="project-card">
    <div class="project-title">💬 Chatbot Inteligente con NLP</div>
    <div class="project-description">
        Asistente virtual con procesamiento de lenguaje natural. Capaz de responder 
        preguntas, realizar tareas y aprender de las interacciones.
    </div>
    <div class="project-tech">
        <strong>Tecnologías:</strong> Python, OpenAI API, LangChain, Streamlit
    </div>
    <a href="https://github.com/tu-usuario/proyecto3" target="_blank" class="project-button">
        🔗 Ver Proyecto en GitHub
    </a>
    <a href="https://tu-chatbot.streamlit.app" target="_blank" class="project-button" style="margin-left: 10px;">
        🌐 Demo en Vivo
    </a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    <p style='font-size: 1.2rem;'><strong>© 2024 Edgar Mirringa</strong></p>
    <p>Hecho con ❤️ y Streamlit</p>
    <p style='margin-top: 1rem;'>
        <a href="mailto:egsamaca56@gmail.com" style="color: #00d4ff; text-decoration: none; margin: 0 10px;">📧 Email</a> | 
        <a href="https://linkedin.com/in/tu-perfil" target="_blank" style="color: #00d4ff; text-decoration: none; margin: 0 10px;">🔗 LinkedIn</a> | 
        <a href="https://github.com/tu-usuario" target="_blank" style="color: #00d4ff; text-decoration: none; margin: 0 10px;">💻 GitHub</a>
    </p>
</div>
""", unsafe_allow_html=True)