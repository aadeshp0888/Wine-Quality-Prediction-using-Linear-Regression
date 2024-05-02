from flask import Flask, render_template, jsonify, request
import pickle
import os
import numpy as np

app = Flask(__name__)
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "model.pkl")

# Load the model using the absolute file path
with open(file_path, "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get variables from the form
        density = float(request.form["density"])
        # Predict using the loaded model
        prediction = model.predict([[density]])
        # Convert NumPy array to Python list
        prediction_list = prediction.tolist()
        return jsonify({"prediction": prediction_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)