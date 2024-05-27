[volver](../crisp-dm/02-conocimiento-de-los-datos.md)

# Diccionario de Datos 

## weatherAUS.csv

### Características numéricas

|||
|--|--|
|MinTemp| Temperatura mínima del aire en grados Celsius.|
|MaxTemp| Temperatura máxima del aire en grados Celsius.|
|Rainfall| Cantidad de lluvia medida en milímetros.|
|Evaporation| Tasa de evaporación medida en milímetros por día.|
|Sunshine| Horas de sol registradas durante el día.|
|**WindGustSpeed**| Velocidad máxima de ráfagas de viento en kilómetros por hora.|
|WindSpeed9am| Velocidad del viento a las 9am en kilómetros por hora.|
|WindSpeed3pm| Velocidad del viento a las 3pm en kilómetros por hora.|
|Humidity9am| Humedad relativa a las 9am en porcentaje.|
|Humidity3pm| Humedad relativa a las 3pm en porcentaje.|
|Pressure9am| Presión atmosférica a las 9am en hectopascales.|
|Pressure3pm| Presión atmosférica a las 3pm en hectopascales.|
|Cloud9am| Cobertura de nubes a las 9am en octas.|
|Cloud3pm| Cobertura de nubes a las 3pm en octas.|
|Temp9am| Temperatura del aire a las 9am en grados Celsius.|
|Temp3pm| Temperatura del aire a las 3pm en grados Celsius.|
|RISK_MM| Cantidad de lluvia del día siguiente en milímetros.|

### Características object
|||
|--|--|
|Date| Fecha de la observación.|
|Location| Ubicación de la estación meteorológica.|
|WindGustDir Dirección de la ráfaga de viento más fuerte.|
|WindDir9am| Dirección del viento a las 9am.|
|WindDir3pm| Dirección del viento a las 3pm.|
|RainToday| Indicador de si ha llovido durante el día.|
|RainTomorrow| Indicador de si se espera lluvia para el día siguiente.|

## weatherAUS_Locations.csv
|||
|--|--|
|Location|Nombre de la ciudad|
|Count|Cantidad de registros metereológicos|
|Latitud|latitud|
|Longitud|longitud|
|Coordinates|referencia geoespacial|
|Is_Coastal|indica si la ciudad esta a menos de 10.000 metros de la costa. (10 kilometros)|

