from API import app
from utils.preprocess_image import preprocess_image
from flask import request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from stable_baselines3 import PPO
import numpy as np

# Load TensorFlow models
ripe_model = load_model('Training/health_model/best_model.keras')

# API route for image prediction
@app.route('/api/models/health', methods=['POST'])
def predict_health():
    # Assuming the image is sent as a file in the request
    image_file = request.files['image']
    image = preprocess_image(image_file.read())
    prediction = ripe_model.predict(np.expand_dims(image, axis=0))
    return jsonify({'prediction': prediction.tolist()[0][0] > 0.5})
