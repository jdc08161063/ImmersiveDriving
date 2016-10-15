import numpy as np
import sys
#sys.path.append('home/caffeNutzer/caffe/python')
#import caffe
import os
from PIL import Image
import caffe
import category_translator as ct
from backend.server.song_database import songs_map

class ImageClassifier:
    def __init__(self): #, network_config_file=None, weights=None):
        #sys.path.append('home/caffeNutzer/caffe/python')

        caffe.set_mode_cpu()
        model_def = '/home/caffeNutzer/data/deploy_alexnet_places365.prototxt'
        model_weights = '/home/caffeNutzer/data/alexnet_places365.caffemodel'
        meanFile = '/home/caffeNutzer/data/places365CNN_mean.binaryproto'


        # if weights is not None:
        #     self.net = caffe.Net(network_config_file, weights, caffe.TEST)
        # else:
        #     self.net = caffe.Net(network_config_file, caffe.TEST)
        self.net = caffe.Net(model_def, model_weights, caffe.TEST)
        self.translator = ct.CategoryTranslator(ournet_categories_file="/home/caffeNutzer/ImmersiveDriving/backend/classifier/config/categories_ournet6.txt",
                                                othernet_categories_file="/home/caffeNutzer/ImmersiveDriving/backend/classifier/config/categories_places365.txt",
                                                translation_othernet_file="/home/caffeNutzer/ImmersiveDriving/backend/classifier/config/categories_translation.txt")

        blob = caffe.proto.caffe_pb2.BlobProto()
        data = open(meanFile, 'rb').read()
        blob.ParseFromString(data)
        arr = np.array(caffe.io.blobproto_to_array(blob))
        out = arr[0].mean(1).mean(1)

        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        self.transformer.set_mean('data', out)
        self.transformer.set_transpose('data', (2,0,1))
        self.transformer.set_raw_scale('data', 255)
        self.transformer.set_channel_swap('data', (2,1,0))

    def classify_image(self, imagePath):
        print imagePath
        #image = caffe.io.load_image('/home/caffeNutzer/data/images/sea_coast.jpg')
        image = caffe.io.load_image(imagePath)
        transformed_image = self.transformer.preprocess('data', image)
        self.net.blobs['data'].data[...] = transformed_image

        output = self.net.forward()
        output_prob = output['prob'][0]
        index_max_prob = output_prob.argmax()
        print 'onlynet', index_max_prob

        label = self.translator.othernet_to_ournet(index_max_prob)
        return songs_map[label], None

    def load_image(self, imageName):
        im = np.array(Image.open(imageName))
        return im, None

if __name__ == "__main__":
    sys.path.append('home/caffeNutzer/caffe/python')
    import caffe
    ic = ImageClassifier()   
    print 'ourlabel', ic.classify_image('/home/caffeNutzer/data/images/valley.jpg')
