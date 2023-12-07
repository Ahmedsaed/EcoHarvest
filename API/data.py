from API import app
from flask import request, jsonify
import pandas as pd
import numpy as np

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
