import numpy as np
from PIL import Image
import caffe
import CategoryTranslator as ct

class ImageClassifier:
    def __init__(self, network_config_file=None):
        caffe.set_mode_cpu()
        self.net = caffe.Net(network_config_file, caffe.TEST)
        self.translator = ct.CategoryTranslator(ournet_categories_file="./config/categories_ournet6.txt",
                                             places_categories_file="./config/categories_places365.txt",
                                             translation_file="./config/categories_translation.txt")

    def classify_image(self, imageName):
        im, err = self.load_image(imageName)
        if err is not None:
            raise ValueError
        x, y, _ = im.shape
        im = np.reshape(im, (1, 3, x, y))
        self.net.blobs['data'].data[...] = im

        probs = self.net.forward()['prob']
        index_max_prob = np.argmax(probs)
        label = self.translator.places365_to_ournet6(index_max_prob)
        return label, None

    def load_image(self, imageName):
        im = np.array(Image.open(imageName))
        return im, None
