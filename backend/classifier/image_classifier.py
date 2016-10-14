import numpy as np
import matplotlib.pyplot as plt
import sys
#sys.path.append('home/caffeNutzer/caffe/python')
#import caffe
import os
from PIL import Image
import caffe
import category_translator as ct

class ImageClassifier:
    def __init__(self): #, network_config_file=None, weights=None):
        #sys.path.append('home/caffeNutzer/caffe/python')

        caffe.set_mode_cpu()
        model_def = '/home/caffeNutzer/data/deploy_alexnet_places365.prototxt'
        model_weights = '/home/caffeNutzer/data/alexnet_places365.caffemodel'

        # if weights is not None:
        #     self.net = caffe.Net(network_config_file, weights, caffe.TEST)
        # else:
        #     self.net = caffe.Net(network_config_file, caffe.TEST)
        self.net = caffe.Net(model_def, model_weights, caffe.TEST)
        self.translator = ct.CategoryTranslator(ournet_categories_file="/home/caffeNutzer/data/config/categories_ournet6.txt",
                                             places_categories_file="/home/caffeNutzer/data/config/categories_places365.txt",
                                             translation_file="/home/caffeNutzer/data/config/categories_translation.txt")

        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        self.transformer.set_transpose('data', (2,0,1))
        self.transformer.set_raw_scale('data', 255)
        self.transformer.set_channel_swap('data', (2,1,0))

    def classify_image(self, imagePath):
        # im, err = self.load_image(imageName)
        # if err is not None:
        #     raise ValueError
        # x, y, _ = im.shape
        # im = np.reshape(im, (1, 3, x, y))
        # self.net.blobs['data'].data[...] = im

        # probs = self.net.forward()['prob']
        # index_max_prob = np.argmax(probs)

        

        #image = caffe.io.load_image('/home/caffeNutzer/data/images/sea_coast.jpg')
        image = caffe.io.load_image(imagePath)
        transformed_image = self.transformer.preprocess('data', image)
        self.net.blobs['data'].data[...] = transformed_image

        output = self.net.forward()
        output_prob = output['prob'][0]
        index_max_prob = output_prob.argmax()
        print 'onlynet', index_max_prob
        
        label = self.translator.places365_to_ournet6(index_max_prob)
        return label, None

    def load_image(self, imageName):
        im = np.array(Image.open(imageName))
        return im, None

if __name__ == "__main__":
    sys.path.append('home/caffeNutzer/caffe/python')
    import caffe
    ic = ImageClassifier()   
    print 'ourlabel', ic.classify_image('/home/caffeNutzer/data/images/sea_coast.jpg')
