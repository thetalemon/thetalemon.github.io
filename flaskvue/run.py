from flask import Flask, render_template, jsonify, request
from random import *
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

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
        return render_template("index.html")
