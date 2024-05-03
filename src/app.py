from flask import Flask, render_template, request
from joblib import load
import pandas as pd

# Inicializar la aplicación Flask
app = Flask(__name__, template_folder='C:/Users/lenovo/Desktop/Proyectos Machine Learning/Bootcamp/aplicacion web de ml usando flask/templates')

# Cargar el modelo entrenado
modelo_salarios = load('C:/Users/lenovo/machine-learning-python-template/models/modelo_salarios.joblib')

# Ruta para la página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para la predicción
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Obtener los datos ingresados por el usuario
            years_experience = float(request.form['years_experience'])
            
            # Hacer la predicción utilizando el modelo cargado
            prediction = modelo_salarios.predict([[years_experience]])[0]
            
            # Renderizar el resultado
            return render_template('result.html', prediction=prediction)
        except Exception as e:
            # Manejar errores
            return render_template('index.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)