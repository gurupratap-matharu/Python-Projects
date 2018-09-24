class Volunteer(object):

    """Makes you make volunteers of different countries for your hostel"""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def getName(self):
        return self.name

    def getCountry(self):
        return self.country

    def __str__(self):
        return "%s is from %s" % (self.name, self.country)


Luis = Volunteer("Luis Briceno", "Venezuela")
Veer = Volunteer("Gurupratap Matharu", "India")
Camila = Volunteer("Camila Cabello", "Brazil")
Gerardo = Volunteer("Gerardo Almoran", "Colombia")
Sophie = Volunteer("Sophie Von deja", "Netherlands")

print(Luis)
print(Veer)
print(Camila)
print(Gerardo)
print(Sophie)

print(Volunteer.getCountry(Sophie))
