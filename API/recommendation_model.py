from API import app
from utils.create_env import create_env
from flask import request, jsonify
from stable_baselines3 import PPO
import numpy as np

# Load RL model
recommendation_model = PPO.load('Training/recommendation_model/best_model.zip')

# API route for numeric prediction
@app.route('/api/models/recommendation', methods=['POST'])
def predict_numeric():
    # Assuming JSON data with temperature, ph, and water level is sent in the request
    data = request.json
    input_data = [data['temperature'], data['ph'], data['water_level']]

    env = create_env()

    obs = env.reset()
    done = False
    score = 0

    while not done:
        action, _ = recommendation_model.predict(obs)
        obs, reward, done, info = env.step(action)
        score += reward

    recommendations = [0, 0, 0] # -1 lower value, 0 no change, 1 increase value

    # compute recommendation if mean squared error is more than 0.5
    if np.abs((obs[0] - input_data[0])) > 2:
        if obs[0] > input_data[0]:
            recommendations[0] = 1
        elif obs[0] < input_data[0]:
            recommendations[0] = -1
        else:
            recommendations[0] = 0

    if np.abs((obs[1] - input_data[1])) > 0.5:
        if obs[1] > input_data[1]:
            recommendations[1] = 1
        elif obs[1] < input_data[1]:
            recommendations[1] = -1
        else:
            recommendations[1] = 0

    if np.abs((obs[2] - input_data[2])) > 5:
        if obs[2] > input_data[2]:
            recommendations[2] = 1
        elif obs[2] < input_data[2]:
            recommendations[2] = -1
        else:
            recommendations[2] = 0

    return jsonify({'prediction': recommendations})
