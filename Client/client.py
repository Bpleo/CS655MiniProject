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
        url1 = "http://140.254.14.107:5000/predict"
        url2 = "http://140.254.14.110:5000/predict"
        url3 = "http://140.254.14.111:5000/predict"
        image = {'img':open(secure_filename(img.filename),'rb')}
        
        start = time.time()
        r1 = requests.post(url1, files=image)
        total_time1 = " VGG16 Total time: {:.3f}s".format(time.time() - start)
        
        start = time.time()
        r2 = requests.post(url2, files=image)
        total_time2 = " RESNET18 Total time: {:.3f}s".format(time.time() - start)
        
        start = time.time()
        r3 = requests.post(url3, files=image)
        total_time3 = " REGNETx8 Total time: {:.3f}s".format(time.time() - start)
        
        print(total_time1)
        print(total_time2)
        print(total_time3
        return render_template('output.html', value1 = r1.text + total_time1, value2 = r2.text + total_time2, value3 = r3.text + total_time3)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
