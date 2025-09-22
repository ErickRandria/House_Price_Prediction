import json
import pickle
from flask import Flask, request, jsonify, render_template, url_for
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
with open('linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')   

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    
    # Convert data into DataFrame
    input_data = pd.DataFrame([data])
    
    # Make prediction using the pre-trained model
    prediction = model.predict(input_data)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
    