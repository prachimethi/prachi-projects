import requests

# API URL
url = "http://127.0.0.1:5000/predict"

# Sample input data (make sure it matches your model's input features)
data = {
    "features": ['price' ,'1h' ,'24h','7d','24h_volume','date','Encoded_coin','price_ma_7','volatility' , 'mkt_cap_capped']
}

# Send POST request
response = requests.post(url, json=data)

# Print the response (prediction)
print("Prediction:", response.json())
