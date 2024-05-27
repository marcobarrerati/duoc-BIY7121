[volver](../02-conocimiento-de-los-datos.ipynb)

## CRS

El CRS (Sistema de Referencia de Coordenadas, por sus siglas en inglés, Coordinate Reference System) es un sistema que utiliza coordenadas para determinar la ubicación de puntos en el espacio. Un CRS define cómo las coordenadas bidimensionales (latitud y longitud, o x e y) se transforman en ubicaciones en la superficie de la Tierra o en otro sistema de referencia.

### Tipos de CRS
CRS Geográficos (Geographic Coordinate Systems, GCS):

#### Basados en una superficie esférica o elipsoidal.
Usan latitud y longitud para definir ubicaciones.
Ejemplo: EPSG:4326 (WGS 84), que es comúnmente utilizado en GPS.
CRS Proyectados (Projected Coordinate Systems, PCS):

#### Basados en una proyección de la superficie de la Tierra en un plano bidimensional.
Usan coordenadas x e y en unidades métricas (metros, kilómetros, etc.).
Ejemplo: EPSG:3857 (Pseudo-Mercator), utilizado en muchos mapas en línea.
Importancia del CRS
El CRS es crucial para la precisión en el análisis geoespacial porque determina cómo se interpretan las coordenadas y cómo se calculan las distancias y áreas. Sin un CRS adecuado, las coordenadas pueden no alinearse correctamente y las distancias calculadas pueden ser incorrectas.

### Ejemplo de uso en GeoPandas
Al trabajar con datos geoespaciales en GeoPandas, es importante asegurarse de que todos los datos tengan el CRS correcto y, si es necesario, reproyectarlos a un CRS adecuado para los cálculos que deseas realizar.

```python
import geopandas as gpd
from shapely.geometry import Point

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'Location': ['A', 'B', 'C'],
    'Latitude': [34.0522, 36.7783, 40.7128],
    'Longitude': [-118.2437, -119.4179, -74.0060]
})

# Crear una columna con la geometría de los puntos
df['Coordinates'] = list(zip(df['Longitude'], df['Latitude']))
df['Coordinates'] = df['Coordinates'].apply(Point)

# Convertir el DataFrame a un GeoDataFrame y asignar un CRS (EPSG:4326 para WGS 84)
gdf = gpd.GeoDataFrame(df, geometry='Coordinates')
gdf.set_crs(epsg=4326, inplace=True)
print(gdf)
```

```python
# Reproyectar a un CRS proyectado (EPSG:3857, Pseudo-Mercator)
gdf_projected = gdf.to_crs(epsg=3857)
print(gdf_projected)
```

### Verificación y Configuración del CRS
Verificar el CRS: gdf.crs muestra el CRS actual del GeoDataFrame.
Asignar un CRS: gdf.set_crs(epsg=4326, inplace=True) asigna un CRS a un GeoDataFrame que no tiene uno definido.
Reproyectar a otro CRS: gdf.to_crs(epsg=3857) reproyecta el GeoDataFrame a un CRS diferente.
