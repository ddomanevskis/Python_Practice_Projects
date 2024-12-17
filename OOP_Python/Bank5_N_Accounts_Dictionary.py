# No OOP
# Bank 5
# Multiple Accounts - Dictionary
accountsList = []


def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name': aName, 'balance': aBalance, 'password': aPassword}
    accountList.append(newAccountDict)


def show(accountNumber):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('     Name', thisAccountDict['name'])
    print('     Balance', thisAccountDict['balance'])
    print('     Password', thisAccountDict['password'])
    print()


def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']


def deposit(accountNumber, amountToDeposit, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None

    accountBalance = thisAccountDict['balance'] + amountToDeposit
    return accountBalance


def withdraw(accountNumber, amountToWithdraw, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount!')
        return None

    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None

    if amountToWithdraw > thisAccountDict['balance']:
        print('Insufficient funds')
        return None

    accountBalance = thisAccountDict['balance'] - amountToWithdraw
    return accountBalance


newAccount('John Doe', 100, 'soup')
newAccount('Mary Joe', 500, 'nouga')


while True:
    print()
    print('Press b to get balance')
    print('Prees d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What would you like to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Enter your password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is', theBalance)

    elif action == 'd':
        print('Deposit:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter the amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter your password: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is', newBalance)

    elif action == 'n':
        print('Create New Account:')
        userName = input('Please enter your name: ')
        userStartingAmount = input('Please enter the starting amount of you initial deposit: ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('Please enter your password: ')
        userAccountNumber = len(accountsList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your account number is:', userAccountNumber)

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 's':
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        print('Show:')
        show(userAccountNumber)

    elif action == 'q':
        break

    else:
        print('Invalid input. Please try again')