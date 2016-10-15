import numpy as np
import matplotlib.pyplot as plt
import sys
#sys.path.append('home/caffeNutzer/caffe/python')
#import caffe
import os
from PIL import Image
import caffe
import category_translator as ct

class FaceClassifier:
    def __init__(self): #, network_config_file=None, weights=None):
        #sys.path.append('home/caffeNutzer/caffe/python')

        caffe.set_mode_cpu()
        model_def = '/home/caffeNutzer/face/deploy.prototxt'
        model_weights = '/home/caffeNutzer/face/EmotiW_VGG_S.caffemodel'
        meanFile = '/home/caffeNutzer/face/mean.binaryproto'
        self.translator = ct.CategoryTranslator(
            ournet_categories_file="/home/caffeNutzer/ImmersiveDriving/backend/classifier/config/categories_faces2.txt",
            othernet_categories_file="/home/caffeNutzer/ImmersiveDriving/backend/classifier/config/categories_faces7.txt",
            translation_othernet_file="/home/caffeNutzer/ImmersiveDriving/backend/classifier/config/categories_translation_faces.txt")

        self.net = caffe.Net(model_def, model_weights, caffe.TEST)
        # incorporate mean subtraction
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

        self.action = "keep"    # can also be "skip"

    def classify_image(self, imagePath):

        image = caffe.io.load_image(imagePath)
        transformed_image = self.transformer.preprocess('data', image)
        self.net.blobs['data'].data[...] = transformed_image

        output = self.net.forward()
        output_prob = output['prob'][0]
        index_max_prob = output_prob.argmax()
        print("maxprob", index_max_prob)
        label = self.translator.othernet_to_ournet(index_max_prob)
        self.action = label
        print("facenetlabel", label)
        return label, index_max_prob

    def load_image(self, imageName):
        im = np.array(Image.open(imageName))
        return im, None

    def get_action(self):
        return self.action

if __name__ == "__main__":
    sys.path.append('home/caffeNutzer/caffe/python')
    import caffe
    ic = FaceClassifier()
    print 'ourlabel0', ic.classify_image('/home/caffeNutzer/ImmersiveDriving/backend/classifier/demo_dataset/faces/happy_strong.jpg')
    print 'ourlabel1', ic.classify_image('/home/caffeNutzer/ImmersiveDriving/backend/classifier/demo_dataset/faces/neutral2.jpg')
    print 'ourlabel2', ic.classify_image('/home/caffeNutzer/ImmersiveDriving/backend/classifier/demo_dataset/faces/disgust2.jpg')