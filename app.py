import numpy as np
from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

# Absolute path to your model file
model_path =  os.path.join(os.path.dirname(__file__), 'model.pkl')

# Load the model safely
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    raise Exception(f"Could not load the model: {e}")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/FindYourCrop', methods=['GET', 'POST'])
def FindYourCrop():
    if request.method == 'POST':
        try:
            # Match input names from HTML
            N = float(request.form['N'])
            P = float(request.form['P'])
            K = float(request.form['K'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            # Log transformation
            K_log = np.log(K + 1)

            # Prediction
            features = np.array([[N, P, K_log, temperature, humidity, ph, rainfall]])
            prediction = model.predict(features)

            return render_template('FindYourCrop.html', prediction=prediction[0])

        except Exception as e:
            return render_template('FindYourCrop.html', prediction=f"⚠️ Error: {e}")
    
    return render_template('FindYourCrop.html')

if __name__ == "__main__":
    app.run(debug=True)
