class Account:
    """This is the main class which creates a bank account for a particular user."""
    branch = "Shoppers Stop Branch, Vile Parle West, Mumbai, India."
    ifsccode = 400093

    def __init__(self):
        """This will initialize each object of the Account class. This is the constructor method."""

    def name(self, firstname, middlename='', lastname=''):
        """This stores the first-name, middle-name and last-name of the each account holder"""
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.fullname = self.firstname + ' ' + self.middlename + ' ' + self.lastname

    def age(self, age):
        """Stores the age of the account holder"""
        self.age = age
        return "Age successfully stored for the account holder called {fullname}!".format(fullname=self.fullname)

    def account_number(self, account_number):
        """Stores the account number for a particular object that is instantiated from the Account class."""
        self.account_number = account_number

    def contact(self, *cellphone, landline, fax, address, email):
        """This method is dedicated to store all contact related information for a particular account holder."""
        self.cellphone = cellphone
        self.landline = landline
        self.fax = fax
        self.address = address
        self.email = email


gurupratap = Account()

gurupratap.name("Gurupratap", lastname="Matharu", middlename="Singh")
gurupratap.account_number(1150254191)
gurupratap.contact(9833000588, 02582 - 224327, "Plot No.8, Tapi Nagar, Yawal Road, Bhusawal, 425201", "gurupratap.matharu@gmail.com")
# gurupratap.age(33)

# print(gurupratap.fullname, end=', ')
# print(gurupratap.account_number, end=', ')
# print(gurupratap.age)
# print(gurupratap.branch)

# print('*' * 60)
