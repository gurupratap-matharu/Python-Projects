class Account:

    """The main account class which is used to create accounts in a bank."""

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as f:
            self.balance = int(f.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as f:
            f.write(str(self.balance))


class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        """Transfers amount to another account."""
        self.balance -= (amount + self.fee)


checking = Checking("balance.txt", 1)
checking.transfer(10)
print(checking.balance)
checking.commit()
