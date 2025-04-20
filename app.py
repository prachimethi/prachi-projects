from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load("notebook/xgb_liquidity_model.pkl")

# Initialize Flask app
app = Flask(__name__)

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON input

    # Convert input to numpy array (make sure it matches feature order & count)
    input_features = np.array(data['features']).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_features)[0]

    return jsonify({'liquidity_ratio_prediction': float(prediction)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
