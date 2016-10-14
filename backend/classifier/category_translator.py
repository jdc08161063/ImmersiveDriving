
""" Convert a Places365 category to a broader one. Input categories are stored in categories_places365.txt file.
The output categories are stored in categories_ournet6.txt """
class CategoryTranslator():

    def __init__(self, ournet_categories_file=None, places_categories_file=None, translation_file=None):
        self.translation_file = translation_file
        self.ournet_categories = self._load_classes_from_file(ournet_categories_file)
        self.places_categories = self._load_classes_from_file(places_categories_file)
        self.translated_categories = self._convert_categories()

    def _load_classes_from_file(self, filename=None):
        categories = dict()
        if filename is not None:
            with open(filename, 'r') as f:
                content = f.readlines()
                for cl in content:
                    catname, num_identifier = cl.split()
                    categories[int(num_identifier)] = catname[3:]
        return categories

    def _convert_categories(self):
        translation_categories = dict()
        with open(self.translation_file) as f:
            content = f.readlines()
            for cl in content:
                _, places_id, ournet_id = cl.split()
                translation_categories[int(places_id)] = int(ournet_id)
        return translation_categories

    """ converts the class.
    Input: String class form the places365 network classes
    Output: String from the OurNet6 classes """
    def places365_to_ournet6(self, cat_id=0):
        return self.ournet_categories[self.translated_categories[cat_id]]


if __name__ == "__main__":
    cu = CategoryTranslator(ournet_categories_file="./config/categories_ournet6.txt",
                      places_categories_file="./config/categories_places365.txt",
                      translation_file="./config/categories_translation.txt")


