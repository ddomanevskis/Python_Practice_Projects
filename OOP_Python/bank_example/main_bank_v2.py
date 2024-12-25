from Account import *

accountsList = []

oAccount = Account('John', 100, 'JohnsPassword')
accountsList.append(oAccount)
print("Jphn's account number is 0")

oAccount = Account('Jane', 200, 'JanesPassword')
accountsList.append(oAccount)
print("Jane's account number is 1")

accountsList[0].show()
accountsList[1].show()
print()

print('Calling methods of the two accounts...')
accountsList[0].deposit(50, 'JohnsPassword')
accountsList[1].withdraw(100, 'JanesPassword')
accountsList[1].deposit(200, 'JanesPassword')

accountsList[0].show()
accountsList[1].show()

print()
userName = input('What is the name for the new user account?')
userBalance = input('What is the starting balance for the new user account?')
userPassword = input('What is the password for the new user account?')
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)

print('Created new account, account number is 2')
accountsList[2].show()

accountsList[2].deposit(100, userPassword)
userBalance = accountsList[2].getBalance(userPassword)
print()
print('After depositing 100, the user balance is', userBalance)

accountsList[2].show()
