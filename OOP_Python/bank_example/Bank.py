from Account import *

class Bank():
    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        self.nextAccountNumber += 1
        return newAccountNumber
    
    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name of the account holder? ')
        userStartingAmount = input('What is the starting balance of the account?')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('Please enter your password:')
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number:')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter your password:')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance, ' Which is now returnd to you.')
            del self.accountsDict[userAccountNumber]
            print('Your account is now closed.')

    def getBalance(self):
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number:')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter your password:')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        accountNum = input('Please enter your account number:')
        accountNum = int(accountNum)
        depositAmount = input('Please enter the deposit amount:')
        depositAmount = int(depositAmount)
        userAccountPassword = input('Please enter your password:')
        oAccount = self.accountsDict[accountNum]
        theBalance = oAccount.deposit(depositAmount, userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('Account number:', userAccountNumber)
            oAccount.show()

    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number:')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Please enter the withdrawal amount:')
        userAmount = int(userAmount)
        userAccountPassword = input('Please enter your password:')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print('Withdraw:', userAmount)
            print('Your balance is:', theBalance)

