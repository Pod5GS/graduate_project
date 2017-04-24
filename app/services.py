import subprocess


def parse_image(imgPath):
    returncode = subprocess.call("sh scripts/parse_image.sh" + imgPath, shell=True)
    if returncode == 0:
        return "success"
    else:
        return "fail"
