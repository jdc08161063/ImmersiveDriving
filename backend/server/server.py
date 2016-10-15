import os
from backend.classifier.image_classifier import ImageClassifier
from flask import json
from flask import Response
from flask import Flask

app = Flask(__name__)


def song_list_for_image(image_name):
    classifier = ImageClassifier()
    song_list, err = classifier.classify_image(
        str(os.path.realpath('.')) + '/backend/classifier/demo_dataset/resized/' + image_name)
    if err is not None:
        print err
        return None
    return {image_name: [song.to_json() for song in song_list]}


def get_image_list():
    image_list = []
    image_dir = str(os.path.realpath('..')) + '/classifier/demo_dataset/resized'
    for fileName in os.listdir(image_dir):
        if fileName.endswith('.jpg') or fileName.endswith('.png'):
            print fileName
            image_list.append(fileName)
    return image_list


@app.route("/all_songs")
def get_all_songs():
    image_list = get_image_list()
    songs_map = map(song_list_for_image, image_list)

    js = json.dumps(songs_map)
    resp = Response(js, status=200, mimetype='application/json', headers=[('Access-Control-Allow-Origin', '*')])
    return resp


@app.route("/<string:image_name>")
def get_song_for_image(image_name):
    print image_name
    songs_map = song_list_for_image(image_name)
    if songs_map is None:
        return Response(status=500)
    js = json.dumps(songs_map)
    resp = Response(js, status=200, mimetype='application/json', headers=[('Access-Control-Allow-Origin', '*')])
    return resp


if __name__ == "__main__":
    app.run()
