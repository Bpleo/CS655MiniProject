from flask import request, Flask, render_template
import requests
import time
import os
from werkzeug.utils import secure_filename
from IRNode import IRNode
import argparse

app = Flask(__name__)
result = ""


@app.route('/predict', methods=['GET', 'POST'])
def recognition():
    if request.method == 'POST':
        img = request.files['img']
        print("fname:" + img.filename)
        img.save(secure_filename(img.filename))
        start_time = time.time()
        parser = argparse.ArgumentParser(description="655 Image Recognition Parser")
        parser.add_argument("--modelType", type=str, default="vgg16", help="model type support:{vgg16,....}")
        parser.add_argument("--modelsDir", type=str, default="models", help="the folder that store the models")
        args = parser.parse_args()
        node = IRNode(args.modelType, args.modelsDir)
        try:
            result = node.predict(secure_filename(img.filename))
            result += "\nProcessing time: {:.3f}s".format(time.time() - start_time)
            return render_template('result.html',value=result)
        except:
            return render_template('result.html',value='Invalid File Type!!')
        
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
