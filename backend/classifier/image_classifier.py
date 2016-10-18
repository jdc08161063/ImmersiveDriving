import os
import numpy as np
import category_translator as ct
import caffe
import urllib

from backend.server.song_database import songs_map


class ImageClassifier:
    def __init__(self,
                 weights_file=os.path.join(os.path.dirname(__file__), 'alexnet_places365.caffemodel'),
                 network_file=os.path.join(os.path.dirname(__file__), 'deploy_alexnet_places365.prototxt'),
                 data_mean_file=os.path.join(os.path.dirname(__file__), 'places365CNN_mean.binaryproto')):
        self.label = None

        caffe.set_mode_cpu()
        self.ensure_model_config(weights_file, network_file, data_mean_file)
        self.net = caffe.Net(network_file, weights_file, caffe.TEST)
        self.translator = ct.CategoryTranslator(
            ournet_categories_file=os.path.join(os.path.dirname(__file__), "config/categories_ournet6.txt"),
            othernet_categories_file=os.path.join(os.path.dirname(__file__), "config/categories_places365.txt"),
            translation_othernet_file=os.path.join(os.path.dirname(__file__), "config/categories_translation.txt"))

        blob = caffe.proto.caffe_pb2.BlobProto()
        data = open(data_mean_file, 'rb').read()
        blob.ParseFromString(data)
        arr = np.array(caffe.io.blobproto_to_array(blob))
        out = arr[0].mean(1).mean(1)

        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        self.transformer.set_mean('data', out)
        self.transformer.set_transpose('data', (2, 0, 1))
        self.transformer.set_raw_scale('data', 255)
        self.transformer.set_channel_swap('data', (2, 1, 0))

    def classify_image(self, image_path):
        print "Serving image: %s" % image_path
        image = caffe.io.load_image(image_path)
        transformed_image = self.transformer.preprocess('data', image)
        self.net.blobs['data'].data[...] = transformed_image

        output = self.net.forward()
        output_prob = output['prob'][0]
        index_max_prob = output_prob.argmax()
        print "Classified as: %s" % index_max_prob

        self.label = self.translator.othernet_to_ournet(index_max_prob)
        return songs_map[self.label], None

    def get_label(self):
        return self.label

    @staticmethod
    def ensure_model_config(weights_file, network_file, mean_file):
        if not os.path.isfile(weights_file):
            print "Downloading model weights ..."
            urllib.urlretrieve(
                "http://places2.csail.mit.edu/models_places365/alexnet_places365.caffemodel",
                weights_file)

        if not os.path.isfile(network_file):
            print "Downloading model architecture ... "
            urllib.urlretrieve(
                "https://raw.githubusercontent.com/metalbubble/places365/master/deploy_alexnet_places365.prototxt",
                network_file)

        if not os.path.isfile(mean_file):
            print "Downloading landscape mean values ... "
            urllib.urlretrieve(
                "https://github.com/metalbubble/places365/blob/master/places365CNN_mean.binaryproto?raw=true",
                mean_file)
