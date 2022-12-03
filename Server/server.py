from flask import request, Flask, render_template
import requests
import time
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
result = ""

@app.route('/predict', methods=['GET', 'POST'])
def recognition():
    if request.method == 'POST':
        img = request.files['img']
        print("fname:" + img.filename)
        img.save(secure_filename(img.filename))
        start_time = time.time()
        
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
