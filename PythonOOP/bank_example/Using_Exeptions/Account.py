class AbortTransaction(Exception):
    '''Raised when a transaction is aborted'''
    pass

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be a number')
        if amount < 0:
            raise AbortTransaction('Amount must be positive')
        return amount
    
    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('Password does not match')
        
    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance += amountToDeposit
        return self.balance
    
    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction('Cannot withdraw more funds than are in the account')
        self.balance -= amountToWithdraw
        return self.balance
    
    def show(self):
        print('Name:', self.name)
        print('Balance:', self.balance)
        print('Password:', self.password)