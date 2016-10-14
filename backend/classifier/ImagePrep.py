import os
from PIL import Image

class ImagePrep():

    def __init__(self, path_to_images=None):
        self.images_folder = path_to_images


    def _resize_to(self, filename=None, x=224, y=224):
        im = Image.open("./"+self.images_folder+"/"+filename)
        im.thumbnail((x, y), Image.ANTIALIAS)
        outname = filename[:-8]
        im.save("./"+self.images_folder+"/resized/"+"{0}.jpg".format(outname))


    def resize_all(self, x, y):
        for filename in os.listdir(self.images_folder):
            if filename.endswith(".jpg"):
                self._resize_to(filename, x=x, y=y)

if __name__ == "__main__":
    ip = ImagePrep("./demo_dataset")
    ip.resize_all(x=224, y=224)
