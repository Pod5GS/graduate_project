import subprocess


def upload_image(dir_path, file):
    filename = file.filename
    path = "/".join([dir_path, filename])
    file.save(path)
    return path


def parse_image(imgPath):
    returncode = subprocess.call("sh scripts/parse_image.sh" + imgPath, shell=True)
    if returncode == 0:
        return "success"
    else:
        return "fail"
