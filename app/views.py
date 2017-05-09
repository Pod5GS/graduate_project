# -*- coding:utf-8 -*-
from flask import render_template, request
from flask import jsonify
from app import app
from services import upload_and_parse
import os

# get the current folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/upload_and_parse', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    model_type = request.form.get('model')
    dir_path = os.path.join(APP_ROOT, 'static/data')
    result = upload_and_parse(dir_path, uploaded_file, model_type)
    return jsonify(result)
