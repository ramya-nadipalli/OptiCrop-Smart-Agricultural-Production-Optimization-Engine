import numpy as np
from flask import Flask, request, render_template
import pickle
import os
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Absolute path to model file - check both possible locations
model_path = os.path.join(os.path.dirname(__file__), 'model', 'model.pkl')
if not os.path.exists(model_path):
    model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

# Load the model safely
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    print("Model loaded OK from: " + model_path)
except Exception as e:
    raise Exception("Could not load the model from " + model_path + ": " + str(e))

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

            # Log transformation on K (as done during training)
            K_log = np.log(K + 1)

            # Prediction
            features = np.array([[N, P, K_log, temperature, humidity, ph, rainfall]])
            prediction = model.predict(features)

            # Capitalize crop name for display
            crop_name = str(prediction[0]).capitalize()

            return render_template('FindYourCrop.html', prediction=crop_name)

        except ValueError:
            return render_template('FindYourCrop.html', prediction="Invalid input: Please enter numeric values only.")
        except Exception as e:
            return render_template('FindYourCrop.html', prediction="Error: " + str(e))

    return render_template('FindYourCrop.html')

if __name__ == "__main__":
    print("OptiCrop - Smart Agricultural Production Optimization Engine")
    print("Starting Flask server at http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
