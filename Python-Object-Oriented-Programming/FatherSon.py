class Other(object):
    def override(self):
        print("Others override function.")

    def implicit(self):
        print("Others implicit function.")

    def altered(self):
        print("Others altered function.")


class Child(object):

    def __init__(self):
        self.other = Other()

    def override(self):
        print("Child's first override statement.")
        self.other.override()
        print("Child's second override statement.")

    def implicit(self):
        self.other.implicit()

    def altered(self):
        print("Child's first alter statement.")
        self.other.altered()
        print("Child's second alter statement.")


son = Child()

son.override()
