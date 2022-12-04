from flask import Flask, render_template, request
import requests
import time
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/upload',methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        img = request.files['img']
        img.save(secure_filename(img.filename))
        url = "http://140.254.14.107:5000/predict"
        image = {'img':open(secure_filename(img.filename),'rb')}
        start = time.time()
        r = requests.post(url, files=image)
        total_time = " Total time: {:.3f}s".format(time.time() - start)
        print(total_time)
        return render_template('output.html', value = r.text + total_time)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
