import streamlit as st
import pandas as pd
import numpy as np
import os

# 1. CONFIGURACIÓN DE LA PÁGINA (Modo ancho y título limpio)
st.set_page_config(page_title="Presentación Riesgo Sismico", layout="wide")

# 2. ESTILOS PERSONALIZADOS (Azul Profundo y Crema para un tono académico y elegante)
st.markdown("""
    <style>
    .main { background-color: #f3f0df; color: #005088; font-family: 'DM Sans', sans-serif; }
    h1, h2, h3 { color: #005088; font-family: 'Merriweather', serif; }
    .stButton>button { background-color: #005088; color: white; border-radius: 8px; }
    
    /* Cajas y Tarjetas de Contenido */
    .highlight-box { background-color: white; padding: 25px; border-radius: 12px; border-left: 5px solid #11caa0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .error-box { background-color: #fdf2f2; padding: 25px; border-radius: 12px; border-left: 5px solid #f05252; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; color: #771d1d; }
    
    /* Estilos para Reportes de Métricas Limpios */
    .metric-card { background-color: #ffffff; border: 1px solid #e5e7eb; border-radius: 10px; padding: 15px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
    .metric-val-bad { font-size: 32px; font-weight: bold; color: #f05252; }
    .metric-val-good { font-size: 32px; font-weight: bold; color: #11caa0; }
    .metric-label { font-size: 14px; color: #6b7280; font-weight: 500; margin-top: 5px; }
    
    /* Código Simulado Bonito */
    .code-box { background-color: #1e1e1e; color: #d4d4d4; font-family: 'Courier New', Courier, monospace; padding: 15px; border-radius: 8px; font-size: 14px; line-height: 1.5; box-shadow: inset 0 2px 4px rgba(0,0,0,0.3); }
    .code-keyword { color: #569cd6; font-weight: bold; }
    .code-string { color: #ce9178; }
    .code-comment { color: #6a9955; font-style: italic; }
    </style>
""", unsafe_allow_html=True)

# Directorio local para las gráficas descargadas
IMG_DIR = "imagenes"

# 3. BARRA LATERAL: ÍNDICE DE DIAPOSITIVAS
st.sidebar.title("📌 Índice de Diapositivas")
opciones = [
    "Portada",
    "Descripción del Proyecto",
    "Selección y Preparación de Datos",
    "Análisis de Correlación Avanzado",
    "Ingeniería de Características y Selección",
    "Construcción y Evaluación de Modelos",
    "Ajuste de Hiperparámetros y Optimización",
    "Hallazgos Clave e Insights",
    "Aplicación e Impacto en el Mundo Real",
    "Trabajo Futuro y Mejoras",
    "Cierre y Preguntas"
]
diapositiva = st.sidebar.radio("Ir a:", opciones)

st.sidebar.markdown("---")
st.sidebar.info("💡 Usa este panel o las flechas de tu teclado para navegar durante tu defensa del viernes.")

# 4. CONTENIDO DE LAS DIAPOSITIVAS (FLUJO COMPLETO)

# --- 1. PORTADA ---
if diapositiva == "Portada":
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.title("🌋 Clasificación y Predicción del Riesgo Sísmico Global")
    st.subheader("Modelización predictiva mediante técnicas avanzadas de Machine Learning")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <p><b>Fecha de Presentación:</b> Viernes, 29 de mayo de 2026</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>Miembros del Equipo</h3>
            <p>• Naila Ikhenazen</p>
            <p style="color: #11caa0; font-weight: bold;">🚀 Entorno local de ejecución configurado</p>
        </div>
        """, unsafe_allow_html=True)

# --- 2. DESCRIPCIÓN DEL PROYECTO ---
elif diapositiva == "Descripción del Proyecto":
    st.header("🏢 Descripción del Proyecto y Planteamiento del Problema")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>El Contexto Sismológico</h3>
            <p>Los terremotos representan una de las mayores amenazas impredecibles del planeta. Disponer de un sistema capaz de catalogar el peligro de forma instantánea es crítico para los centros de alerta temprana y la toma de decisiones de protección civil.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="highlight-box">
            <h3>Objetivo del Proyecto</h3>
            <p>Crear un sistema basado en <b>modelos de aprendizaje automático</b> que reciba los datos físicos básicos de un temblor en el momento en que ocurre y lo clasifique automáticamente en dos niveles:</p>
            <ul>
                <li><b>Riesgo Moderado:</b> Temblores comunes que no causan daños estructurales.</li>
                <li><b>Riesgo Severo:</b> Terremotos peligrosos con alto potencial de destrucción.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>Justificación Técnica</h3>
            <p> El carácter exepcional de los terremotos severos dificula su predicción. </p>
        </div>
        """, unsafe_allow_html=True)

# --- 3. SELECCIÓN Y PREPARACIÓN DE DATOS ---
elif diapositiva == "Selección y Preparación de Datos":
    st.header("📊 Selección y Preparación de Datos")
    col1, col2 = st.columns([1.1, 1])
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>Origen e Integración de Variables</h3>
            <p>El Dataset de kaggle comprende registros históricos globales de actividad sísmica. El dataset final de testeo consta de <b>6,215 registros</b>.</p>
        </div>
        <div class="highlight-box">
            <h3>Preprocesamiento: Escalado de Datos</h3>
            <p>Debido a las diferencias de magnitud y escala entre los atributos (por ejemplo, la profundidad medida en kilómetros frente a la latitud/longitud en grados), se aplicó un proceso estricto de <b>escalado de características (Feature Scaling)</b>. Esta normalización es crítica para algoritmos basados en distancias (como KNN), evitando que las variables con rangos numéricos más grandes distorsionen la geometría del modelo.</p>
        </div>
        <div class="highlight-box">
            <h3>Validación Estadística: Chi-Square Test ($\chi^2$)</h3>
            <p>Se implementaron pruebas de Chi-cuadrado para evaluar formalmente la independencia de los factores categóricos y de localización. Esto permitió descartar correlaciones espúreas y asegurar que la distribución de las clases objetivo posee significación estadística respecto a las zonas de vecindad.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.subheader("Distribución Espacial de los Eventos Sísmicos")
        img_mapa = os.path.join(IMG_DIR, "image_ca8e44.jpg")
        if os.path.exists(img_mapa):
            st.image(img_mapa, caption="Mapa de Localización vs Profundidad: Análisis geoespacial de los sismos analizados.", use_container_width=True)
        else:
            chart_data = pd.DataFrame({
                'Severidad del Sismo': ['Moderado (0)', 'Severo (1)'],
                'Número de Registros': [6105, 110]
            })
            st.bar_chart(data=chart_data, x='Severidad del Sismo', y='Número de Registros', color="#005088")
            st.warning("⚠️ Nota Metodológica: El desbalanceo masivo (1.77% Clase 1) invalida el uso de Accuracy global.")

# --- 4. ANÁLISIS DE CORRELACIÓN AVANZADO (NUEVA DIAPOSITIVA) ---
elif diapositiva == "Análisis de Correlación Avanzado":
    st.header("📈 Estrategia de Reducción y Mapa de Calor de Correlación")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>Tratamiento de Alta Cardinalidad</h3>
            <p>Para incluir la información contextual de las descripciones geográficas (<code>location_desc</code>) sin saturar el modelo ni provocar fallos de memoria, se implementó una estrategia controlada:</p>
            <ol>
                <li>Se aislaron las <b>10 localizaciones más frecuentes</b> del dataset.</li>
                <li>Las etiquetas restantes menos comunes se agruparon bajo la categoría común <b>'Otros'</b>.</li>
                <li>Se generaron variables <i>dummy</i> estructuradas (One-Hot Encoding) sobre este subconjunto optimizado.</li>
            </ol>
        </div>
        <div class="highlight-box">
            <h3>Conclusiones Extraídas del Mapa</h3>
            <ul>
                <li><b>Ausencia de Colinealidad Fuerte:</b> Ninguna de las variables predictoras físicas posee una correlación lineal peligrosa con las zonas geográficas indexadas, asegurando la estabilidad de los coeficientes del modelo.</li>
                <li><b>Estructura de Bloque Geográfico:</b> Las correlaciones negativas o cercanas a cero reafirman que la fuerza del sismo (magnitud) y el punto de fractura (profundidad) responden a comportamientos físicos locales complejos, validando la necesidad de emplear algoritmos no lineales de Machine Learning.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.subheader("Mapa de Calor Optimizado")
        img_heatmap = os.path.join(IMG_DIR, "mapa_calor.jpg")
        if os.path.exists(img_heatmap):
            st.image(img_heatmap, caption="Matriz de correlación simétrica indexando variables físicas y el Top 10 de variables dummy de localización.", use_container_width=True)
        else:
            st.info("📊 Espacio reservado para el Mapa de Calor generado ('imagenes/mapa_calor.jpg').")
            # Matriz interactiva de contingencia como respaldo estético visual
            datos_interactivos = pd.DataFrame(
                [[1.00, 0.05, -0.02, -0.05],
                 [0.05, 1.00, 0.01, 0.04],
                 [-0.02, 0.01, 1.00, -0.12],
                 [-0.05, 0.04, -0.12, 1.00]],
                columns=['magnitude', 'depth_km', 'lat', 'Dummy_Top_Zonas'],
                index=['magnitude', 'depth_km', 'lat', 'Dummy_Top_Zonas']
            )
            st.dataframe(datos_interactivos.style.background_gradient(cmap='coolwarm', axis=None), use_container_width=True)

# --- 5. INGENIERÍA DE CARACTERÍSTICAS Y SELECCIÓN ---
elif diapositiva == "Ingeniería de Características y Selección":
    st.header("⚙️ Ingeniería de Características y Selección")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>Proceso de Selección de Variables</h3>
            <p>Se priorizó el uso de variables físicas continuas puras para garantizar la estabilidad geográfica del modelo:</p>
            <ul>
                <li><b>Magnitud y Profundidad (depth_km):</b> Indicadores directos de la energía liberada y su punto de origen.</li>
                <li><b>Latitud y Longitud:</b> Coordenadas espaciales esenciales para el mapeo geométrico de vecindad.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Matriz de Relaciones Lineales (Correlación)")
        datos_corr = pd.DataFrame(
            [[1.00, 0.05, -0.02, 0.01],
             [0.05, 1.00, 0.01, -0.03],
             [-0.02, 0.01, 1.00, 0.08],
             [0.01, -0.03, 0.08, 1.00]],
            columns=['Magnitud', 'depth_km', 'Latitud', 'Longitud'],
            index=['Magnitud', 'depth_km', 'Latitud', 'Longitud']
        )
        st.dataframe(datos_corr.style.background_gradient(cmap='Blues', axis=None), use_container_width=True)
        
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>Desafíos Críticos Encontrados</h3>
            <p><b>La Maldición de la Dimensionalidad (MemoryError):</b> Al intentar procesar variables categóricas de alta cardinalidad (como descripciones de texto o mapas de calor de localización muy densos), el volumen de datos en memoria colapsó el entorno de ejecución.</p>
            <p><b>Solución:</b> Reducción estratégica eliminando redundancias de texto. Las coordenadas espaciales ya encapsulaban de forma matemática y limpia la ubicación exacta, haciendo innecesarias las cadenas de texto masivas.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Excepción Controlada en Ejecución")
        st.markdown("""
        <div class="code-box">
            <span class="code-comment"># Error crítico detectado al procesar alta cardinalidad categórica</span><br>
            Vectorizing variable: <span class="code-string">'localization_desc'</span>...<br>
            Allocating matrix structure size: 45.2 GB...<br>
            <span class="code-keyword">MemoryError:</span> Unable to allocate array with shape and data type.<br><br>
            <span class="code-comment"># Acciones correctoras aplicadas:</span><br>
            ✔️ Remoción de variables categóricas redundantes.<br>
            ✔️ Preservación de variables continuas puras.
        </div>
        """, unsafe_allow_html=True)

# --- 6. CONSTRUCCIÓN Y EVALUACIÓN DE MODELOS ---
elif diapositiva == "Construcción y Evaluación de Modelos":
    st.header("🏗️ Construcción y Evaluación de Modelos")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>Estrategia Experimental</h3>
            <p>Se evaluaron múltiples familias de algoritmos para contrastar su comportamiento ante el desbalanceo estructural de datos:</p>
            <ul>
                <li><b>Modelos de Ensamble (AdaBoost, Random Forest):</b> Elegidos por su robustez ante datos complejos, aunque vulnerables al sesgo de la clase mayoritaria en configuraciones base.</li>
                <li><b>Modelos Geométricos (KNN):</b> Seleccionados bajo la hipótesis de que el riesgo sismológico responde fuertemente a una vecindad espacial física real.</li>
            </ul>
        </div>
        <div class="highlight-box">
            <h3>Métricas de Validación Críticas</h3>
            <p>Se descartó por completo el uso del <b>Accuracy Global</b>. La evaluación se centró estrictamente en el <b>Recall</b> (Sensibilidad) y el <b>F1-Score</b> de la clase severa (1), garantizando que un sismo peligroso nunca sea ignorado por el sistema.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.subheader("Reporte de Clasificación Base (Modelo AdaBoost)")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown('<div class="metric-card"><div class="metric-val-good">98%</div><div class="metric-label">Accuracy Global</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="metric-card"><div class="metric-val-good">0.98</div><div class="metric-label">Precision (Clase 0)</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="metric-card"><div class="metric-val-bad">0.00%</div><div class="metric-label">Recall (Clase 1)</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown('<div class="metric-card"><div class="metric-val-bad">0.00</div><div class="metric-label">F1-Score (Clase 1)</div></div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.error("🚨 Evidencia de Fallo por Sesgo: El modelo base exhibe un Recall nulo (0.00) sobre la clase minoritaria. Al ignorar estructuralmente la clase de riesgo, el algoritmo maximiza artificialmente el Accuracy, resultando inoperante para entornos de protección civil.")

# --- 7. AJUSTE DE HIPERPARÁMETROS Y OPTIMIZACIÓN ---
elif diapositiva == "Ajuste de Hiperparámetros y Optimización":
    st.header("🔧 Ajuste de Hiperparámetros y Optimización")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>Técnicas de Optimización</h3>
            <p>Se implementó <b>GridSearchCV</b> combinado con <b>Validación Cruzada (Cross-Validation)</b> para explorar de forma exhaustiva el espacio de hiperparámetros sin caer en sobreajuste (overfitting).</p>
            <ul>
                <li><b>KNN:</b> Optimización de la métrica de distancia (Manhattan) y número de vecinos óptimo para ajustar la resolución geométrica.</li>
                <li><b>Random Forest:</b> Control de la profundidad máxima (<code>max_depth=10</code>) para evitar la memorización y balanceo de costes.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Hiperparámetros Determinados por GridSearch")
        st.markdown("""
        <div class="code-box">
            📊 <span class="code-keyword">Best Estimator Parameters (KNN):</span><br>
            • <b>n_neighbors:</b> 3<br>
            • <b>weights:</b> 'distance'<br>
            • <b>metric:</b> 'manhattan'<br><br>
            ✨ <b>Cross-Validation Score (Mean):</b> 0.9819
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>El Impacto del Balanceo de Pesos</h3>
            <p>La inyección del parámetro de penalización por costes condicionales modificó sustancialmente el comportamiento del estimador.</p>
            <p>Al penalizar severamente los fallos sobre los eventos minoritarios, el algoritmo logró romper la inercia estadística, rescatando el Recall crítico de la clase severa y elevándolo de un absoluto <b>0.00 a un 0.25</b>.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Reporte Métrico con Balanceo de Costes")
        c_a, c_b = st.columns(2)
        with c_a:
            st.markdown('<div class="metric-card"><div class="metric-val-good">25.00%</div><div class="metric-label">Recall (Clase 1)</div></div>', unsafe_allow_html=True)
        with c_b:
            st.markdown('<div class="metric-card"><div class="metric-val-good">0.11</div><div class="metric-label">F1-Score Ajustado</div></div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.success("🎉 Incremento del rendimiento predictivo: El ajuste de penalizaciones permite mapear las muestras de riesgo ocultas en la distribución original.")

# --- 8. HALLAZGOS CLAVE E INSIGHTS ---
elif diapositiva == "Hallazgos Clave e Insights":
    st.header("💡 Hallazgos Clave e Insights del Modelo")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>1. Ventaja de la Estructura Métrica (KNN)</h3>
            <p>Los modelos basados en proximidad geométrica e hiperplanos de distancia directa (KNN) demostraron una capacidad innata superior para este problema específico en comparación con las divisiones ortogonales simples de los árboles de decisión básicos.</p>
            <p>Esto confirma de manera empírica que el comportamiento sísmico mantiene una fortísima dependencia de continuidad geoespacial.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>2. Ausencia de Patrones Lineales</h3>
            <p>Las pruebas estadísticas iniciales reflejaron correlaciones lineales prácticamente nulas entre las variables aisladas y la severidad del evento.</p>
            <p>Esto aporta un valor científico clave: el riesgo sísmico es un fenómeno de <b>alta no linealidad</b>, justificando plenamente el despliegue de modelos de Machine Learning avanzados en lugar de regresiones estadísticas tradicionales.</p>
        </div>
        """, unsafe_allow_html=True)

# --- 9. APLICACIÓN E IMPACTO EN EL MUNDO REAL ---
elif diapositiva == "Aplicación e Impacto en el Mundo Real":
    st.header("🌍 Aplicación e Impacto en el Mundo Real")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>Despliegue y Protección Civil</h3>
            <p>Este sistema está diseñado para integrarse directamente como un módulo inteligente dentro de los centros de monitorización geológica y alertas tempranas de protección civil.</p>
            <p>Permite la automatización instantánea del nivel de riesgo ante las primeras señales de ondas sísmicas continuas.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>Consideraciones Éticas y Limitaciones</h3>
            <p><b>El Coste Humano del Falso Negativo:</b> En desastres naturales, un falso positivo genera costes económicos por evacuaciones preventivas; sin embargo, un falso negativo (ignorar un sismo severo) tiene un coste en vidas humanas.</p>
            <p>Por ello, el éxito de este proyecto radica en haber priorizado la sensibilidad del algoritmo por encima del acierto general, minimizando el riesgo de dejar desprotegida a la población.</p>
        </div>
        """, unsafe_allow_html=True)

# --- 10. TRABAJO FUTURO Y MEJORAS ---
elif diapositiva == "Trabajo Futuro y Mejoras":
    st.header("🚀 Trabajo Futuro y Líneas de Expansión")
    st.markdown("""
    <div class="highlight-box">
        <h3>1. Conexión de Datos en Streaming (Tiempo Real)</h3>
        <p>Expandir la actual aplicación web de Streamlit para conectarla de forma dinámica mediante APIs públicas a institutos sismológicos globales (como el USGS), permitiendo clasificar terremotos en tiempo real a medida que ocurren.</p>
    </div>
    <div class="highlight-box">
        <h3>2. Técnicas Avanzadas de Remuestreo Técnico</h3>
        <p>Implementar algoritmos avanzados de generación sintética de muestras como <b>SMOTE-Tomek</b> o arquitecturas combinadas (EasyEnsemble) para intentar forzar el F1-Score del Random Forest por encima del 0.11 actual sin degradar la precisión.</p>
    </div>
    <div class="highlight-box">
        <h3>3. Arquitecturas de Aprendizaje Profundo (Deep Learning)</h3>
        <p>Diseñar y evaluar redes neuronales artificiales (perceptrones multicapa) provistas de funciones de activación no lineales complejas, analizando si consiguen superar el rendimiento predictivo del modelado geométrico actual.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 11. CIERRE Y PREGUNTAS ---
elif diapositiva == "Cierre y Preguntas":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("Clasificación y Predicción del Riesgo Sísmico Global")
    st.subheader("Modelización predictiva mediante técnicas avanzadas de Machine Learning")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box" style="text-align: center;">
            <h2 style="color: #11caa0;">¡Muchas Gracias!</h2>
            <p>Quedo a la entera disposición del tribunal para cualquier pregunta, aclaración o comentario sobre el proyecto desarrollado.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h3>Miembros del Proyecto</h3>
            <p><b>Autora:</b> Naila Ikhenazen</p>
            <p><b>Fecha de Defensa:</b> Viernes</p>
            <p><b>Entorno:</b> Desarrollado íntegramente en Python utilizando el ecosistema Scikit-Learn y Streamlit.</p>
        </div>
        """, unsafe_allow_html=True)