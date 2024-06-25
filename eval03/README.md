# Evaluación Parcial 03 

## Proceso de Evaluación

### [Preparación de entorno](ENV.md)

### Preprocesamiento de Datos

* Imputación de valores faltantes.
* Codificación de variables categóricas.
* Normalización de datos.

# Modelos No Supervisados

## [K-Means Clustering](mns/k-means-clustering.ipynb)

Es un algoritmo de agrupamiento que particiona los datos en k grupos en los que cada dato pertenece al grupo con la media más cercana.
Puede ser útil para identificar patrones en los datos meteorológicos sin etiquetas previas.

```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
labels = kmeans.labels_
```


## [DBSCAN (Density-Based Spatial Clustering of Applications with Noise)](mns/dbscan.ipynb)

Es un algoritmo de clustering basado en la densidad que puede encontrar clusters de cualquier forma y manejar ruido.
Es útil para identificar patrones meteorológicos y anomalías sin la necesidad de especificar el número de clusters.

```python
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan.fit(data)
labels = dbscan.labels_
```


## [PCA (Principal Component Analysis)](mns/pca.ipynb)

Aunque PCA no es un modelo de clustering, es una técnica de reducción de dimensionalidad que transforma las variables originales en un nuevo conjunto de variables no correlacionadas (componentes principales).
Puede ser útil para visualizar y explorar la estructura de los datos meteorológicos.

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data)
```


# Modelos Supervisados

* Evaluación de Modelos Supervisados
    * Métricas de Evaluación
        * Exactitud (Accuracy)
        * Precisión, Recall, F1-Score
        * Curva ROC y AUC


## [Regresión Logística](ms/regresion_logistica.ipynb)

Es un modelo de clasificación que se utiliza para predecir la probabilidad de un resultado binario.
Puede ser útil para predecir eventos meteorológicos binarios como "lloverá o no lloverá".

```python
from sklearn.linear_model import LogisticRegression
logistic_regression = LogisticRegression()
logistic_regression.fit(X_train, y_train)
y_pred = logistic_regression.predict(X_test)
```

## [Random Forest](ms/random_forest.ipynb)

Es un modelo de aprendizaje conjunto basado en múltiples árboles de decisión.
Puede manejar tanto tareas de clasificación como de regresión y es robusto frente al sobreajuste, lo que lo hace adecuado para predecir diversas variables meteorológicas.

```python
from sklearn.ensemble import RandomForestClassifier
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, y_train)
y_pred = random_forest.predict(X_test)
```


## [Gradient Boosting (XGBoost)](ms/gradient_boosting.ipynb)

Es un algoritmo de aprendizaje conjunto que crea modelos de predicción a partir de una serie de árboles de decisión.
Es conocido por su alta precisión y eficiencia, adecuado para tareas de predicción de eventos meteorológicos complejos.

```python
import xgboost as xgb
xgboost_model = xgb.XGBClassifier()
xgboost_model.fit(X_train, y_train)
y_pred = xgboost_model.predict(X_test)
```





