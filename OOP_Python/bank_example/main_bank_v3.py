from Account import *
accountsDict = {}
nextAccountNumber = 0

oAccount = Account('John', 100, 'JohnsPassword')
johnsAccountNumber = nextAccountNumber
accountsDict[johnsAccountNumber] = oAccount
print('Account number for Joe is:', johnsAccountNumber)
nextAccountNumber += 1

oAccount = Account('Jane', 200, 'JanesPassword')
janesAccountNumber = nextAccountNumber
accountsDict[janesAccountNumber] = oAccount
print('Account number for Mary is:', janesAccountNumber)
nextAccountNumber += 1

accountsDict[johnsAccountNumber].show()
accountsDict[janesAccountNumber].show()
print()

print('Calling methods of the two accounts...')
accountsDict[johnsAccountNumber].deposit(50, 'JohnsPassword')
accountsDict[janesAccountNumber].withdraw(100, 'JanesPassword')
accountsDict[janesAccountNumber].deposit(200, 'JanesPassword')

accountsDict[johnsAccountNumber].show()
accountsDict[janesAccountNumber].show()

print()
userName = input('what is the name for the new user account?')
userBalance = input('what is the starting balance?')
userBalance = int(userBalance)
userPassword = input('what is the password for the user?')
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
print('Created new account, account number is:', newAccountNumber)
nextAccountNumber += 1

accountsDict[newAccountNumber].show()

accountsDict[newAccountNumber].deposit(100, userPassword)
usersBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print('After depositing 100, the user balance is:', usersBalance)

accountsDict[newAccountNumber].show()
