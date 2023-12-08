from API import app
from flask import request, jsonify
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Load the CSV file
data = pd.read_csv('./dummy_data.csv')

# API routes for each column
@app.route('/api/data/temperature', methods=['GET'])
@app.route('/api/data/temperature/<int:n>', methods=['GET'])
def get_temperature(n=5):
    return jsonify(data['temperature'].head(n).to_dict())

@app.route('/api/data/light_intensity', methods=['GET'])
@app.route('/api/data/light_intensity/<int:n>', methods=['GET'])
def get_light_intensity(n=5):
    return jsonify(data['light_intensity'].head(n).to_dict())

@app.route('/api/data/co2_level', methods=['GET'])
@app.route('/api/data/co2_level/<int:n>', methods=['GET'])
def get_co2_level(n=5):
    return jsonify(data['co2_level'].head(n).to_dict())

@app.route('/api/data/water_ph_value', methods=['GET'])
@app.route('/api/data/water_ph_value/<int:n>', methods=['GET'])
def get_water_ph_value(n=5):
    return jsonify(data['water_ph_value'].head(n).to_dict())

@app.route('/api/data/time', methods=['GET'])
@app.route('/api/data/time/<int:n>', methods=['GET'])
def get_time(n=1):
    return jsonify(data['time'].head(n).to_dict())

@app.route('/api/data/update', methods=['PUT'])
def update_data():
    # Assume the JSON format is {'temperature': value, 'light_intensity': value, 'co2_level': value, 'water_ph_value': value}
    request_data = request.json


    # Update the data with the new values
    data.loc[len(data)] = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        request_data['temperature'],
        np.random.uniform(100, 1000),
        np.random.uniform(300, 800),
        request_data['ph']
    ]

    return jsonify({"message": "Data updated successfully"}), 200


@app.teardown_appcontext
def save_data(*args, **kwargs):
    # Save the data to the CSV file
    data.to_csv('./dummy_data.csv', index=False)
