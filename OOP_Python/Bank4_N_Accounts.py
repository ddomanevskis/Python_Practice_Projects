# No OOP
# Bank 4
# Multiple Accounts
accountNamesList = []
accountBalancesList = []
accountPasswordsList = []


def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)


def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('Account', accountNumber)
    print('     Name', accountNamesList[accountNumber])
    print('     Balance', accountBalancesList[accountNumber])
    print('     Password', accountPasswordsList[accountNumber])
    print()


def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]


def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None

    accountBalance = accountBalancesList[accountNumber] + amountToDeposit
    return accountBalance


def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList

    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount!')
        return None

    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None

    if amountToWithdraw > accountBalancesList[accountNumber]:
        print('Insufficient funds')
        return None

    accountBalance = accountBalancesList[accountNumber] - amountToWithdraw
    return accountBalance


newAccount('John Doe', 100, 'soup')
newAccount('Mary Joe', 500, 'nouga')


while True:
    print()
    print('Press b to get balance')
    print('Prees d to make a deposit')
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
