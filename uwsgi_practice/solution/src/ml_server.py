from flask import  Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def add():
    numbers = request.json
    prediction = regressor.predict(np.array(numbers).reshape(1, -1))[0]
    return jsonify({'prediction':prediction})    

if __name__ == '__main__':
    with open('hw1.pkl', 'rb') as pkl_file:
        regressor = pickle.load(pkl_file)

    app.run('localhost', 5000)    