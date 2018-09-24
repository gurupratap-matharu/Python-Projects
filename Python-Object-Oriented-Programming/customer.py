""" I am going to practice the purpose of python classes and OOP style of programming here. Still I'm not exactly sure about how it works and would like to experiment a bit.

Here, we want to create a customer class. It represent the customer of a bank."""


class Customer(object):

    """This represents the customer class. It takes in the name and the initial balance as its arguments."""

    def __init__(self, name):
        """The constructor method. We initialize only the customer here with the name."""
        self.name = name

    def set_balance(self, balance=0.0):
        """Here we set the balance of the customer. Default amount is 0."""
        self.balance = balance

    def withdraw(self, amount):
        """This method is used to withdraw money from the account. If withdrawal amount is greater than the balance in the customer's account then an error message is raised."""
        if amount <= 0:
            print("Withdrawal amount should be a positive number.")
        elif amount > self.balance:
            raise RuntimeError('Not sufficient funds in your account.')

        else:
            self.balance -= amount
            print("Withdrawal of %s done successfully. Your remaining balance is %s" % (amount, self.balance))

    def deposit(self, amount):
        """This method is used to deposit *amount* money into the bank account."""
        if amount <= 0:
            print("Deposit money should be greater than zero.")

        else:
            self.balance += amount
            print("You account has been successfully credited with %s. Your remaining balance is %s" % (amount, self.balance))


veer = Customer("Veerpratap")
veer.set_balance(1000)
veer.withdraw(5)
