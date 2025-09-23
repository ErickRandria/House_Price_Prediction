# app.py

from flask import Flask, request, render_template
import numpy as np
import pickle

# Load trained model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Extract values from form
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)
    scaled_features = scaler.transform(final_features)
    prediction = model.predict(scaled_features)

    return render_template("index.html", 
                           prediction_text=f"Predicted House Value: ${prediction[0]*100000:.2f}")

if __name__ == "__main__":
    app.run(debug=True)
