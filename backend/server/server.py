import os
from flask import json
from flask import Response
from flask import Flask
app = Flask(__name__)


def labelimage(imagename):
    return "label"


def getimagenameslist():
    imagenameslist = []
    for fileName in os.listdir(str(os.path.realpath(''))+'/images'):
        if fileName.__contains__('.jpg'):
            imagenameslist.append(fileName)
    return imagenameslist


@app.route("/")
def hello():
    testmap = map(labelimage, getimagenameslist())
    js = json.dumps(testmap)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run()