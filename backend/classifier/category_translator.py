
""" Convert a Places365 category to a broader one. Input categories are stored in categories_places365.txt file.
The output categories are stored in categories_ournet6.txt """
class CategoryTranslator():

    def __init__(self, ournet_categories_file=None,
                 othernet_categories_file=None,
                 translation_othernet_file=None):
        self.ournet_categories = self._load_classes_from_file(ournet_categories_file)
        self.places_categories = self._load_classes_from_file(othernet_categories_file)
        self.translated_categories = self._convert_categories(translation_othernet_file)

    def _load_classes_from_file(self, filename=None):
        categories = dict()
        if filename is not None:
            with open(filename, 'r') as f:
                content = f.readlines()
                for cl in content:
                    catname, num_identifier = cl.split()
                    categories[int(num_identifier)] = catname[3:]
        return categories

    def _convert_categories(self, translation_file=None):
        translation_categories = dict()
        with open(translation_file) as f:
            content = f.readlines()
            for cl in content:
                _, places_id, ournet_id = cl.split()
                translation_categories[int(places_id)] = int(ournet_id)
        return translation_categories

    """ converts the class.
    Input: String class form the places365/faces network classes
    Output: String from the OurNet6/ourfaces classes """
    def othernet_to_ournet(self, cat_id=0):
        return self.ournet_categories[self.translated_categories[cat_id]]




