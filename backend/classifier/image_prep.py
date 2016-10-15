import os
from PIL import Image
from scipy import misc
import numpy as np

class ImagePrep():

    def __init__(self, path_to_images=None, x=224, y=224):
        self.new_x = x
        self.new_y = y
        self.images_folder = path_to_images
        self.images = self._load_resized_images(path_to_images)
        self.center_all()

    def _load_resized_images(self, path):

        #resize first
        for i, filename in enumerate(os.listdir(self.images_folder)):
            if filename.endswith(".jpg"):
                im = Image.open("./" + self.images_folder + "/" + filename)
                im = im.resize((self.new_x, self.new_y), Image.ANTIALIAS)
                im.save("./" + self.images_folder + "/resized/" + filename)

        # now load as np arrays
        images = list()
        for i, filename in enumerate(os.listdir(self.images_folder + "/resized/")):
            if filename.endswith(".jpg"):
                images.append(misc.imread(path+"/resized/"+filename))
        images = np.asarray(images)

        return images

    def center_all(self):
        # load mean congif data
        pass


if __name__ == "__main__":
    ip = ImagePrep("./demo_dataset")