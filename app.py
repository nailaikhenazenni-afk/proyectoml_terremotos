import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os

# Configuración de la página
st.set_page_config(page_title="Presentación Riesgo Sísmico", layout="wide")

# Estilos personalizados
st.markdown("""
    <style>
    .main { background-color: #f3f0df; color: #005088; font-family: 'DM Sans', sans-serif; }
    h1, h2, h3 { color: #005088; font-family: 'Merriweather', serif; }
    .highlight-box { background-color: white; padding: 25px; border-radius: 12px; border-left: 5px solid #11caa0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .metric-number { font-size: 42px; font-weight: bold; color: #11caa0; font-family: 'Merriweather', serif; }
    </style>
""", unsafe_allow_html=True)

# Ruta base para las imágenes
IMG_DIR = "imagenes"

# --- NAVEGACIÓN ---
st.sidebar.title("📌 Índice de Diapositivas")
opciones = [
    "1. Portada",
    "2. Descripción del Proyecto",
    "3. El Desafío del Desbalanceo",
    "4. Ingeniería de Características (Descartes)",
    "5. El Colapso de los Modelos Base",
    "6. Sintonización y Corrección",
    "7. Conclusiones y Cierre"
]
diapositiva = st.sidebar.radio("Ir a:", opciones)

# --- DIAPOSITIVAS ---

if diapositiva == "1. Portada":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("Clasificación y Predicción del Riesgo Sísmico Global")
    st.subheader("Modelización predictiva mediante técnicas avanzadas de Machine Learning")
    st.markdown("---")
    st.write("**Presentado por:** Tu Nombre")
    st.info("💡 Consejo: Usa las flechas del teclado o el menú lateral para avanzar.")

elif diapositiva == "2. Descripción del Proyecto":
    st.header("🏢 Descripción del Proyecto")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>Problema Central</h3>
            <p>Clasificación automatizada de eventos sismológicos en categorías de riesgo: <b>Moderados (0)</b> frente a <b>Severos (1)</b>.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>Objetivo Técnico</h3>
            <p>Construir un modelo capaz de identificar patrones no lineales en variables físicas puras, evitando métricas globales engañosas.</p>
        </div>
        """, unsafe_allow_html=True)

elif diapositiva == "3. El Desafío del Desbalanceo":
    st.header("📊 El Desafío Crítico: Distribución de Clases")
    
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="highlight-box">
            <h3>Análisis del Soporte</h3>
            <p>El dataset de prueba cuenta con:</p>
            <ul>
                <li><b>Clase 0 (Moderados):</b> 6,105 sismos</li>
                <li><b>Clase 1 (Severos):</b> 110 sismos</li>
            </ul>
            <p>La clase de interés crítico representa únicamente el <b>1.77%</b> del volumen total de los datos.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        # Simulación de la gráfica de barras para impactar visualmente
        datos_desbalanceo = pd.DataFrame({
            'Clase Sísmica': ['Moderados (0)', 'Severos (1)'],
            'Soporte (Registros)': [6105, 110]
        })
        st.bar_chart(data=datos_desbalanceo, x='Clase Sísmica', y='Soporte (Registros)', color="#005088")

elif diapositiva == "4. Ingeniería de Características (Descartes)":
    st.header("⚙️ Ingeniería de Características y Gestión de Recursos")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>1. El Bloqueo por Memoria (MemoryError)</h3>
            <p>Al intentar aplicar técnicas de codificación por categorías sobre descripciones de texto masivas, el sistema colapsó por falta de direccionamiento físico.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Muestra tu captura del MemoryError (image_ca7b0b.png)
        img_path = os.path.join(IMG_DIR, "image_ca7b0b.png")
        if os.path.exists(img_path):
            st.image(img_path, caption="Evidencia del desbordamiento de memoria al vectorizar variables de texto de alta cardinalidad.", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>2. Solución: Matriz de Correlación</h3>
            <p>Se evaluaron las correlaciones lineales. Al demostrarse coeficientes cercanos a cero respecto a la magnitud física, se justificó el descarte de las variables de localización de texto redundantes, salvando el coste computacional.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Muestra tu matriz de correlación (image_ca8e44.jpg)
        img_path_corr = os.path.join(IMG_DIR, "image_ca8e44.jpg")
        if os.path.exists(img_path_corr):
            st.image(img_path_corr, caption="Matriz de correlación reducida analizada.", use_container_width=True)

elif diapositiva == "5. El Colapso de los Modelos Base":
    st.header("❌ El Efecto Espejismo de los Modelos Base")
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>Análisis del Reporte de AdaBoost</h3>
            <p>Los ensambles tradicionales sin balancear caen en una inercia estadística absoluta:</p>
            <ul>
                <li><b>Accuracy del 98%:</b> Un valor sobresaliente pero completamente <b>falso e inútil</b>.</li>
                <li><b>Recall de 0.00 en Clase 1:</b> El modelo es incapaz de identificar un solo sismo severo.</li>
                <li><b>F1-Score de 0.00:</b> Inoperabilidad absoluta para la toma de decisiones de seguridad civil.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        # Muestra tu reporte de AdaBoost (image_bbef68.png)
        img_path_ada = os.path.join(IMG_DIR, "image_bbef68.png")
        if os.path.exists(img_path_ada):
            st.image(img_path_ada, caption="Reporte de clasificación real de AdaBoost base sin técnicas de compensación.", use_container_width=True)

elif diapositiva == "6. Sintonización y Corrección":
    st.header("🔧 Optimización de Modelos y Rescate de Sensibilidad")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>1. Enfoque Geométrico (KNN)</h3>
            <p>Al aplicar <b>GridSearchCV</b>, se descubrieron los parámetros óptimos espaciales.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Muestra el tuning de KNN (image_ca15aa.png)
        img_path_knn = os.path.join(IMG_DIR, "image_ca15aa.png")
        if os.path.exists(img_path_knn):
            st.image(img_path_knn, caption="Resultado del tuning para el algoritmo geométrico.", use_container_width=True)
            
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>2. Corrección de Pesos (Random Forest)</h3>
            <p>Forzamos al algoritmo a penalizar los fallos de la clase minoritaria mediante <code>class_weight='balanced'</code>.</p>
            <p><b>¡Impacto Directo!</b> El Recall de la clase severa se elevó de <b>0.00 a un 0.25</b> de sensibilidad real.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Muestra el reporte corregido de Random Forest (image_ca6fe6.png)
        img_path_rf = os.path.join(IMG_DIR, "image_ca6fe6.png")
        if os.path.exists(img_path_rf):
            st.image(img_path_rf, caption="Métricas del Random Forest corregido tras la inyección de pesos balanceados.", use_container_width=True)

elif diapositiva == "7. Conclusiones y Cierre":
    st.title("¡Muchas gracias por su atención!")
    st.subheader("¿Tienen alguna pregunta?")
    st.markdown("---")
    st.markdown("""
    * **Lección de Ingeniería:** El éxito de un modelo ante riesgos naturales extremos reside en sus métricas de sensibilidad (*Recall*), nunca en su acierto global (*Accuracy*).
    * **Hardware:** Los problemas de recursos se solucionan mediante análisis matemático preliminar de características, no forzando la computación.
    """)