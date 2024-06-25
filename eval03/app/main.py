from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
random_forest_model = joblib.load('random_forest_model.pkl')

# Ruta para hacer predicciones
@app.route('/predict', methods=['POST'])
def predict():
    # Obtener datos del cuerpo de la solicitud POST
    data = request.get_json(force=True)
    
    # Preprocesar los datos (ejemplo: convertir a DataFrame de pandas)
    new_data = pd.DataFrame(data)
    
    # Hacer predicciones
    predictions = random_forest_model.predict(new_data)
    
    # Preparar la respuesta como JSON
    response = {'predictions': predictions.tolist()}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
