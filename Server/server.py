from PIL import Image
from flask import request, Flask, render_template
import time
import requests
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
        url = "http://140.254.14.103:5000/"
        try:
            print(secure_filename(img.filename))
            result = node.predict(Image.open(secure_filename(img.filename)))
            result += "Processing time: {:.3f}s".format(time.time() - start_time)
            return result
        except Exception as e:
            print(e.args)
            print(str(e))
            print(repr(e))          
            return "Invalid File Type"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
