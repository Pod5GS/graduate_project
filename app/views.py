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


@app.route('/upload_and_parse', methods=['POST'])
def upload():
    upload_file = request.files['file']
    dir_path = os.path.join(APP_ROOT, 'static/data')
    upload_image(dir_path, upload_file)
    path = 'static/data/' + upload_file.filename
    parse_image(upload_file.filename)
    return jsonify({
        'path': path,
        'name': upload_file.filename
    })
