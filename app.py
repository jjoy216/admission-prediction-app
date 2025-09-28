# create the flask app
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load your model
with open('admission_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    gre = float(data['gre'])
    toefl = float(data['toefl'])
    cgpa = float(data['cgpa'])
    university_rating = float(data['university_rating'])
    sop = float(data['sop'])
    lor = float(data['lor'])
    research = int(data['research'])
    features = np.array([[gre, toefl, cgpa, university_rating, sop, lor, research]])
    prediction = model.predict(features)[0]
    return jsonify({'prediction': float(prediction)})

if __name__ == '__main__':
    app.run(debug=True)