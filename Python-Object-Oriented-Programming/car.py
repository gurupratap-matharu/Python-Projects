class Car(object):
    """Our class method for making different types of cars.
       Basically we'll be practising static methods and decorators in this example."""

    wheels = 4

    def __init__(self, make, model):
        """The basic constructor class. It's a good practice to pass on the
           initialization variables here itself to avoid confusion later."""

        self.make = make
        self.model = model

    def average(self, mileage):
        """Set the mileage for a particular car"""
        self.mileage = mileage
        print("Mileage of %s has been set for %s" % (self.mileage, self.model))

    @staticmethod
    def make_car_sound():
        print("ZOOOOOOMMMMMMMMM")


mustang = Car('Ford', 'Mustang')
maruti = Car('Maruti', 'Maruti-800')


maruti.make_car_sound()
mustang.make_car_sound()
