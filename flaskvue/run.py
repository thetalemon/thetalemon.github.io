from flask import Flask, render_template, jsonify, request
from random import *
from datetime import datetime
import numpy as np
import cv2
import os
import string
import random
import base64

app = Flask(__name__,
                    static_folder = "./dist/static",
                                template_folder = "./dist")

SAVE_DIR = "./images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

def random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

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

@app.route('/cannyFile', methods=['POST'])
def upload():
    # if request.files['image']:
    # 画像として読み込み
    # if request.method != 'POST':
    # return make_response(jsonify({'result': 'invalid method'}), 400)


    base64_png = request.form['image']
    print("base64",base64_png)
    code = base64.b64decode(base64_png.split(',')[1])  # remove header
    image_decoded = Image.open(BytesIO(code))
    image_decoded.save(Path(app.config['SAVE_DIR']) / 'image.png')

    # stream = request.files['image'].stream
    # name = img.filename
    # path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    # img.save(path)

    # img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
    # img = cv2.imdecode(img_array, 1)
    #
    # # 変換
    # img = cv2.Canny(image, 100, 200)
    #
    # # 保存
    # dt_now = datetime.now().strftime("%Y_%m_%d%_H_%M_%S_") + random_str(5)
    # save_path = os.path.join(SAVE_DIR, dt_now + ".png")
    # cv2.imwrite(save_path, img)
    #
    # print("save", save_path)
    # return make_response(jsonify({'result': 'success'})
    # return jsonify(image_decoded)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
        return render_template("index.html")
