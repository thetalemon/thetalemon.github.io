from flask import Flask, render_template, jsonify, request
from random import *
import cv2
import string
import utils
import prosImage

app = Flask(__name__,
                    static_folder = "./dist/static",
                                template_folder = "./dist")

@app.route("/api/testpost", methods=['POST'])
def hello():
    response = {
        "result": int(request.json["val1"].split()[0])*2
    }
    return jsonify(response)

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/cannyFile', methods=['POST'])
def upload():
    base64_png = request.form['image']
    img_array = utils.base64toCV2(base64_png)

    processedImg = prosImage.cannyImage(img_array)
    calcedRGB = prosImage.calcRGB(img_array)

    resultImage = utils.CV2toBase64(processedImg)
    response = {
        'result': resultImage,
        'red'   : calcedRGB[0],
        'green' : calcedRGB[1],
        'blue'  : calcedRGB[2]
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
        return render_template("index.html")
