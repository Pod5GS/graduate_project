import subprocess


def upload_image(dir_path, file):
    filename = file.filename
    path = "/".join([dir_path, filename])
    file.save(path)
    return path


def parse_image(imgName):
    cmd = "sh app/scripts/parse_image.sh " + imgName

    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)

    stdout, stderr = p.communicate()

    if p.returncode == 0:
        print stdout
        return True
    else:
        print stderr
        return False
