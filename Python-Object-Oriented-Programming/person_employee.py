class Person:

	def __init__(self, first, last):
		self.firstname = first
		self.lastname = last
	def __str__(self):
		return self.firstname + " " + self.lastname

class Employee(Person):
	
	def __init__(self, first, last, staffnum):
		Person.__init__(self, first, last)
		self.staffnumber = staffnum

	def GetEmployee(self):
		return self.firstname + " " + self.lastname + ", " + self.staffnumber


