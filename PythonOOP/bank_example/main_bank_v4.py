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

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do?')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number:')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter your password:')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('*** Deposit ***')
        userAccountNumber = input('Please enter your account number:')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter the deposit amount:')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter your password:')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'o':
        print('*** Open Account ***')
        userName = input('Please enter your name:')
        userStartingAmount = input('Please enter the starting amount:')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('Please enter your password:')
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print('Your account number is:', nextAccountNumber)
        nextAccountNumber += 1
        print()

    elif action == 's':
        print('Show:')
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print('Account number:', userAccountNumber)
            oAccount.show()

    elif action == 'q':
        break

    elif action == 'w':
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number:')
        userAccountNumber = int(userAccountNumber)
        userWithdrawalAmount = input('Please enter the withdrawal amount:')
        userWithdrawalAmount = int(userWithdrawalAmount)
        userPassword = input('Please enter your password:')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount, userPassword)
        if theBalance is not None:
            print('Withdraw:', userWithdrawalAmount)
            print('Your balance is:', theBalance)

    else:
        print('Invalid input. Please try again.')

print('Done')
