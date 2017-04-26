from flask import render_template, request
from flask import jsonify
from app import app
from services import upload_image, parse_image
import os

# get the current folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    dir_path = os.path.join(APP_ROOT, '../sceneparsing/data/')
    path = upload_image(dir_path, file)
    color_map_path = '../sceneparsing/result/'
    return render_template("index.html")
