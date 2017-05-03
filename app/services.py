# -*- coding:utf-8 -*-
import subprocess
import os
from utils import generate_random_sequence


def upload_and_parse(dir_path, uploaded_file):
    filename = uploaded_file.filename
    path = "/".join([dir_path, filename])
    uploaded_file.save(path)
    cmd = "sh app/scripts/parse_image.sh " + filename

    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)

    stdout, stderr = p.communicate()

    if p.returncode == 0:
        path = 'static/data/' + filename
        random_sequence = generate_random_sequence()
        color_map_path = 'static/result/colormap' + random_sequence + '.png'
        prediction_path = 'static/result/prediction' + random_sequence + '.png'
        # rename the colormap and prediction
        os.rename('app/static/result/colormap.png', 'app/' + color_map_path)
        os.rename('app/static/result/prediction.png', 'app/' + prediction_path)
        # build return dict
        result = {
            'status': 0,
            'path': path,
            'name': filename,
            'color_map_path': color_map_path,
            'prediction_path': prediction_path
        }
        return result
    else:
        print stderr
        result = {
            'status': 1
        }
        return result
