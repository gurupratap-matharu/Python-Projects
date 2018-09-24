class Human(object):
	
	def __init__(self, name, planet, religious=True):
		self.name = name
		self.planet = planet
		self.religious = religious




class Man(Human):
	
	def __init__(self, name, age):
		Human.__init__(self, name, "Earth")
		self.age = age

class Woman(Human):

	def __init__(self, name, age):
		Human.__init__(self, name, "Earth")
		self.age = age

Newton = Man("Isaac", 33)
Einstein = Man("Albert", 37)
Marie = Woman("Marie Curie", 44)

Veer = Human("Veer", 41)

 
