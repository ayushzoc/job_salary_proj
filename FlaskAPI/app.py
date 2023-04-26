import flask
from flask import Flask, jsonify, request
import json
import pickle
from data_input import data_in
import numpy as np


def predict():
 response = json.dumps({'response': 'yahhhh!'})
 return response, 200

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])

def predict():
    # parse input features from request
    request_json = request.get_json()
    x = request_json['input']
    x_in = np.array(x).reshape(1, -1)
    # load model
    model = load_models()
    prediction = model.predict(x_in)[0]
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
   application.run(debug=True)