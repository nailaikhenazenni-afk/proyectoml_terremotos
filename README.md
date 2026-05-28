# Clasificación y Predicción del Riesgo Sísmico Global mediante Aprendizaje Automático

## Descripción del Proyecto

Este proyecto desarrolla un ecosistema predictivo basado en Machine Learning para la clasificación de eventos sísmicos en dos categorías: Moderados (0) y Severos (1). Utilizando registros históricos globales, el análisis abarca desde la exploración estadística de los datos y el tratamiento de un desbalanceo extremo de clases, hasta la sintonización de hiperparámetros de los modelos no lineales más eficaces.
---

## Objetivo del proyecto

identificar con precisión los factores físicos y geoespaciales que determinan la severidad de un sismo, sirviendo como una herramienta técnica para la gestión de riesgos y la toma de decisiones en seguridad civil.

---

## Estructura del Conjunto de Datos

El modelo se alimenta exclusivamente de variables físicas universales y continuas, garantizando su capacidad de generalización global sin depender de nomenclaturas locales:

- magnitude: Magnitud del evento sísmico en la escala correspondiente.
- depth_km: Profundidad del foco de ruptura (hipocentro) expresada en kilómetros.
- lat: Latitud numérico-espacial del epicentro
- lon: Longitud numérico-espacial del epicentro

Nota metodológica: Se evaluó la inclusión de variables categóricas de texto (localization_desc) mediante One-Hot Encoding. No obstante, tras analizar la matriz de correlación, se descartaron para prevenir problemas de alta dimensionalidad y redundancia informativa (multicolinealidad) respecto a las coordenadas geográficas continuas.


---

## Workflow del proyecto

Eleccíon del tema y del Dataset sobre el cual se va a trabajar 
↓  
Hipótesis  
↓  
Enfoque analítico  
↓  
Comprensión de datos  
↓  
Limpieza de datos  
↓  
Transformación de datos  
↓  
EDA  
↓  
Spltit Test 
↓  
S 
↓  
Visualización y Dashboard  
↓  
Insights y Recomendaciones  

---

## Herramientas utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Tableau
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## KPIs analizados

### Completion Rate
Porcentaje de usuarios que llegan al paso de confirmación.

### Average Time Between Steps
Tiempo promedio entre pasos del proceso.

### Error Rate
Usuarios que retroceden pasos durante el proceso.

### Funnel Analysis
Abandono de usuarios a lo largo del flujo digital.

---

## Hypothesis Testing

### Hipótesis nula ($H_0$)

La tasa de finalización del grupo Test es igual a la del grupo Control.

### Hipótesis alternativa ($H_a$)

El grupo Test presenta mejor rendimiento que el grupo Control.

### Métodos estadísticos

- Two-Proportion Z-Test
- Comparación A/B
- Análisis de performance

---

## Insights principales

- El grupo Test obtuvo una mayor tasa de finalización respecto al grupo Control.
- Existe una pérdida progresiva de usuarios a lo largo del funnel.
- Algunos pasos generan mayor fricción y abandono.
- El rediseño mejora el rendimiento general del proceso digital.

---

## Dashboard Tableau

El dashboard incluye:

- Completion Rate
- Comparación Test vs Control
- Funnel Analysis
- Average Time Between Steps
- Filtros interactivos
- Segmentación de usuarios

---

## Estructura del proyecto

```bash
vanguard-ab-test/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── tableau/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_kpis_hypothesis_testing.ipynb
│   └── 05_final_analysis.ipynb
│
├── tableau/
│
├── slides/
│
├── README.md
│
└── requirements.txt
```

---

## Instalación

Clonar repositorio:

```bash
git clone https://github.com/yourusername/vanguard-ab-test.git
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar notebooks:

```bash
jupyter notebook
```

---

## Conclusiones

El análisis sugiere que el nuevo diseño digital mejora el rendimiento del proceso y genera una experiencia más eficiente para el usuario.

La variación Test superó al grupo Control en los principales KPIs del experimento.

---

## Próximos pasos

Posibles mejoras futuras:

- Segmentación avanzada
- Behavioral Analysis
- Session Path Analysis
- Power Analysis
- Modelos predictivos
- Streamlit App

---

.Estructura del Conjunto de DatosEl modelo se alimenta exclusivamente de variables físicas universales y continuas, garantizando su capacidad de generalización global sin depender de nomenclaturas locales:magnitude: Magnitud del evento sísmico en la escala correspondiente.depth_km: Profundidad del foco de ruptura (hipocentro) expresada en kilómetros.lat: Latitud numérico-espacial del epicentro.lon: Longitud numérico-espacial del epicentro.Nota metodológica sobre ingeniería de características: Se evaluó la inclusión de variables categóricas de texto (localization_desc) mediante One-Hot Encoding. No obstante, tras analizar la matriz de correlación, se descartaron para prevenir problemas de alta dimensionalidad y redundancia informativa (multicolinealidad) respecto a las coordenadas geográficas continuas.Flujo Metodológico1. Análisis Exploratorio y Selección de VariablesSe ejecutó una prueba estadística de Chi-cuadrado para validar la relevancia estructural de las variables, obteniendo un p-valor concluyente de $1.34 \times 10^{-67}$, lo que confirmó la existencia de un patrón sísmico real y no aleatorio en la distribución geográfica.A su vez, la matriz de correlación lineal de Pearson reflejó coeficientes cercanos a cero entre las variables físicas aisladas y la magnitud, demostrando que el fenómeno sísmico presenta un comportamiento no lineal complejo que requiere enfoques de Machine Learning avanzado.2. El Desafío del Desbalanceo ExtremoEl conjunto de datos de prueba presentó un desbalanceo crítico: 6,105 sismos moderados frente a apenas 110 severos (la clase crítica representa solo el 1.7% del total).Al entrenar algoritmos de ensamble tradicionales en su configuración base (como Bagging, AdaBoost y Random Forest), los modelos colapsaron arrojando un Accuracy engañoso del 98% pero ceros absolutos en Precision y Recall para la clase severa. Los algoritmos optimizaban el error global ignorando el evento minoritario.3. Selección y Optimización de ModelosPara solucionar este sesgo, se focalizaron los recursos computacionales en refinar las dos arquitecturas con mayor potencial analítico mediante GridSearchCV enfocado en el F1-Score:K-Nearest Neighbors (KNN): Consolidado como el modelo más eficaz con un score del 98.19% en test. Al operar mediante proximidad geoespacial directa en lugar de optimizaciones de pérdida globales, demostró una capacidad sobresaliente para mapear clústeres de riesgo en el espacio tridimensional.Hiperparámetros óptimos: n_neighbors: 3, metric: 'manhattan', weights: 'distance'.Random Forest (Corregido): Se sintonizó la estructura para romper la inercia de la clase mayoritaria introduciendo penalizaciones balanceadas.Hiperparámetros óptimos: class_weight: 'balanced', max_depth: 10, criterion: 'gini'.Resultado: Se rescató la sensibilidad del modelo, elevando el Recall de la clase severa de 0.00 a un 25% y estabilizando el Macro Average en un 0.60 interpretativo.Tecnologías UtilizadasLenguaje: PythonAnálisis de Datos & Gráficos: Pandas, NumPy, Matplotlib, SeabornMachine Learning: Scikit-Learn (GridSearchCV, KNeighborsClassifier, RandomForestClassifier, tree)Resultados Principales