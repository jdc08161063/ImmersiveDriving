import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class ImageClassifier:
    def __init__(self):
        pass

    def classify_image(self, imageName):
        im, err = self.load_image(imageName)
        if err is not None:
            raise ValueError
        return "label", None

    def load_image(self, imageName):
        im = np.array(Image.open(imageName))
        return im, None
