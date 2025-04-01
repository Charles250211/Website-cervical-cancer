
from flask import Blueprint, render_template, jsonify, request
import os
import requests

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template('index.html')
