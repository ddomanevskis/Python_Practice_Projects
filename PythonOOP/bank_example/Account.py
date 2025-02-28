# Account class

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Incorrect password')
            return None

        if amountToDeposit < 0:
            print('Cannot deposit a negative amount')
            return None

        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect password')
            return None

        if amountToWithdraw < 0:
            print('Cannot withdraw a negative amount')
            return None

        if amountToWithdraw > self.balance:
            print('You do not have enough funds to withdraw this amount')
            return None

        self.balance -= amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Incorrect password')
            return None
        return self.balance

    def show(self):
        print('Name:', self.name)
        print('Balance:', self.balance)
        print('Password', self.password)
        print()
