from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from joblib import load
import json
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
cors = CORS(app)
model_in = load('xgb_model.joblib')

df = pd.read_csv('features.csv')

scaler = StandardScaler()
scaled_features = pd.DataFrame(data=scaler.fit_transform(df), columns=['BHK', 'Total_Sq.ft', 'Price_per_sq.ft', 'Region'])

def get_key(val):
  with open('regions.json') as f:
    regions = json.load(f)
  for key, value in regions.items():
    if val == value:
      return key
  return "key doesn't exist"

@app.route('/', methods=['GET'])

@app.route('/', methods=['GET', 'POST'])
def predict_price():
  if request.method == 'GET':
    return 'hello'
  elif request.method == 'POST':
    x = np.zeros(4)
    data = request.get_json()
    val = get_key(data['region'])
    x[0] = float(data['bhk'])
    x[1] = float(data['total_sq_ft'])
    x[2] = float(data['price_per_sq_ft'])
    x[3] = val
    print(data)
    x_scaled = scaler.transform([x])
    prediction = model_in.predict(x_scaled)[0]
    dict = {"predicted_price": str(prediction)}
    
    return jsonify(dict)
  

if __name__ == '__main__':
  app.run(debug=True)