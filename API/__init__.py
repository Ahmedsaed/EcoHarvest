from flask import Flask

app = Flask(__name__)

from API import data, recommendation_model, ripe_model, health_model
