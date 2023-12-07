from API import app
from utils import preprocess_image
from flask import request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from stable_baselines3 import PPO
import numpy as np

# Load TensorFlow models
ripe_model = load_model('Training/ripe_model/model.keras')

# API route for image prediction
@app.route('/api/models/ripe', methods=['POST'])
def predict_image():
    # Assuming the image is sent as a file in the request
    image_file = request.files['image']
    image = preprocess_image(image_file)
    prediction = ripe_model.predict(np.expand_dims(image, axis=0))
    return jsonify({'prediction': prediction.tolist()})

# # Load RL model
# recommendation_model = PPO.load('Training/recommendation_model/best_model.zip')

# # API route for numeric prediction
# @app.route('/api/models/recommendation', methods=['POST'])
# def predict_numeric():
#     # Assuming JSON data with temperature, ph, and water level is sent in the request
#     data = request.json
#     input_data = [data['temperature'], data['ph'], data['water_level']]

#     prediction = numeric_model.predict(np.array([input_data]))
#     return jsonify({'prediction': prediction.tolist()})
