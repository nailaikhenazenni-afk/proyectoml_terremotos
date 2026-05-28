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
- Feature Scaling
- Feature Selection
↓  
Entrenamiento de los modelos (Machin Learning)
↓  
- Aplicación de hyperparámetros (Hyperparameter Tuning)
- Aplicación de hyperparámetros avanzados (Balence)
↓  
Insights y Recomendaciones  

---

## Herramientas utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn (GridSearchCV, KNeighborsClassifier, RandomForestClassifier, tree)
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## Flujo Metodológico

- 1 Análisis Exploratorio y Selección de Variables

Se ejecutó una prueba estadística de Chi-cuadrado para validar la relevancia estructural de las variables, obteniendo un p-valor concluyente de 1.34x10-67, lo que confirmó la existencia de un patrón sísmico real y no aleatorio en la distribución geográfica.

A su vez, la matriz de correlación lineal de Pearson reflejó coeficientes cercanos a cero entre las variables físicas aisladas y la magnitud, demostrando que el fenómeno sísmico presenta un comportamiento no lineal complejo que requiere enfoques de Machine Learning avanzado 

- 2 El Desafío del Desbalanceo Extremo

El conjunto de datos de prueba presentó un desbalanceo crítico: 6,105 sismos moderados frente a apenas 110 severos (la clase crítica representa solo el 1.7% del total).Al entrenar algoritmos de ensamble tradicionales en su configuración base (como Bagging, AdaBoost y Random Forest), los modelos colapsaron arrojando un Accuracy engañoso del 98% pero ceros absolutos en Precision y Recall para la clase severa. 

Los algoritmos optimizaban el error global ignorando el evento minoritario.

- 3 Selección y Optimización de Modelos 

Para solucionar este sesgo, se focalizaron los recursos computacionales en refinar las dos arquitecturas con mayor potencial analítico mediante GridSearchCV enfocado en el F1-Score:K-Nearest Neighbors (KNN): Consolidado como el modelo más eficaz con un score del 98.19% en test. 

Al operar mediante proximidad geoespacial directa en lugar de optimizaciones de pérdida globales, demostró una capacidad sobresaliente para mapear clústeres de riesgo en el espacio tridimensional.

Hiperparámetros óptimos: n_neighbors: 3, metric: 'manhattan', weights: 'distance'.

Random Forest (Corregido): Se sintonizó la estructura para romper la inercia de la clase mayoritaria introduciendo penalizaciones balanceadas.Hiperparámetros óptimos: class_weight: 'balanced', max_depth: 10, criterion: 'gini'.Resultado: Se rescató la sensibilidad del modelo, elevando el Recall de la clase severa de 0.00 a un 25% y estabilizando el Macro Average en un 0.60 interpretativo.

---

## Insights principales

- Árbol de Decisión Base

Se limitó deliberadamente la profundidad del árbol a 4 niveles para auditar las reglas lógicas del algoritmo. El nodo raíz identificó de forma matemática que la profundidad (depth_km) es la variable con mayor poder de división inicial. 

El modelo logró aislar con un 100% de pureza geométrica (Gini = 0.0) focos críticos de sismos severos en zonas geográficas específicas.

- Comparativa de Modelos (Clase Severa)  

Modelo      Configuración   Precision(Clase 1) Recall(Clase 1) F1-Score(Clase 1) MacroAvgRecall Bagging       Por defecto    0.00                 0.00            0.00           0.50           RandomForest  Por defecto    0.00                 0.00            0.00           0.50
AdaBoost      Por defecto    0.00                 0.00            0.00           0.50
Gradient      Por defecto    0.11                 0.02            0.03           0.51
Boosting
Random        Optimizado     0.07                 0.25            0.11           0.60
Forest        (Tuning)

KNN          Optimizado     -                     -              98,17%           -
             (Tuning)


---

## Estructura del proyecto

```bash
vanguard-ab-test/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│  
│
├── proyctoml_terremotos.ipynb
```
---

## Instalación

Clonar repositorio:

```bash
git clone https://github.com/yourusername/proyectoml-terremotos.git
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

- Los fenómenos naturales con desbalanceo extremo no pueden evaluarse mediante la métrica de Accuracy, siendo el F1-Score y el Recall los verdaderos indicadores de viabilidad en la gestión de riesgos.

- Las técnicas basadas en optimización de pérdidas e iteraciones de árboles colapsan ante la masa de la clase mayoritaria a menos que se apliquen correcciones explícitas de pesos (class_weight='balanced').

- La localización física tridimensional (lat, lon, depth_km) actúa como el predictor más robusto, convirtiendo a los modelos de vecindad geométrica (KNN) en la solución tecnológica óptima para este escenario predictivo.


---

## Próximos pasos

Otros posibles fócos de análisis:

- Predicción de la Profundidad del Foco (Regresión)

La profundidad de un sismo determina en gran medida el daño que causa en la superficie (los más superficiales suelen ser más destructivos). Podríamos intentar predecir la profundidad a partir de la localización y la magnitud.

Algoritmos sugeridos: Regresión Lineal, o un Regresor de Random Forest.

- Análisis de Réplicas (Clasificación Binaria) 
Predecir si un terremoto principal de gran magnitud generará una réplica de magnitud mayor a 5.0 en las siguientes 48 horas dentro de un radio de acción determinado.

- Intentar predecir cuándo o dónde ocurrirá un sismo usando series temporales avanzadas (opción más complejos)


---

