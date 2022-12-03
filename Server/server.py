from flask import request, Flask, render_template
import requests
import time
import os
from werkzeug.utils import secure_filename
from classifier import ImageRecognition

app = Flask(__name__)
result = ""

@app.route('/predict', methods=['GET', 'POST'])
def recognition():
    if request.method == 'POST':
        img = request.files['img']
        img.save(secure_filename(img.filename))
        start_time = time.time()
        try:
            result = 
