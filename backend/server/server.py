import os
from backend.classifier.image_classifier import ImageClassifier
from flask import json
from flask import Response
from flask import Flask
app = Flask(__name__)


def labelimage(imagefilename):
    classifier = ImageClassifier()
    label, err = classifier.classify_image(str(os.path.realpath('..'))+'/classifier/demo_dataset/resized/'+imagefilename)
    if err is not None:
        return None

    return label


def getimagenameslist():
    imagenameslist = []
    image_dir = str(os.path.realpath('..'))+'/classifier/demo_dataset/resized'
    for fileName in os.listdir(image_dir):
        if fileName.endswith('.jpg') or fileName.endswith('.png'):
            print fileName
            imagenameslist.append(fileName)

    return imagenameslist


@app.route("/labelslist")
def getlabelslist():
    imagenameslist = getimagenameslist()
    labelsmap = map(labelimage, imagenameslist)
    result = []
    for index, member in enumerate(imagenameslist):
        pair = {
            imagenameslist[index] : labelsmap[index]
        }
        result.append(pair)

    js = json.dumps(result)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route("/<string:imagefilename>")
def getlabel(imagefilename):
    label = labelimage(imagefilename)
    if label is None:
        return Response(status=400)

    pair = {
        imagefilename : label
    }
    js = json.dumps(pair)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run()