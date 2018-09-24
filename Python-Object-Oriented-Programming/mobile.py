class Mobile(object):

    """A class which represent mobile phones"""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def getBrand(self):
        return self.brand

    def getModel(self):
        return self.model

    def __str__(self):
        return "%s is an %s" % (self.model, self.brand)

