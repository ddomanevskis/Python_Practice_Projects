# No OOP
# Bank 3
# Two Accounts
account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccounts = 0


def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password


def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('Account 0')
        print('     Name', account0Name)
        print('     Balance', account0Balance)
        print('     Password', account0Password)
        print()
    if account1Name != '':
        print('Account 1')
        print('     Name', account1Name)
        print('     Balance', account1Balance)
        print('     Password', account1Password)
        print()


def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
        return account0Balance
    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None
        return account1Balance


def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount!')
            return None
        if password != account0Password:
            print('Incorrect password')
            return None

        account0Balance = account0Balance + amountToDeposit
        return account0Balance
    if accountNumber == 1:
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount!')
            return None
        if password != account1Password:
            print('Incorrect password')
            return None

        account1Balance = account1Balance + amountToDeposit
        return account1Balance


def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount!')
            return None

        if password != account0Password:
            print('Incorrect password')
            return None

        if amountToWithdraw > account0Balance:
            print('Insufficient funds')
            return None

        account0Balance = account0Balance - amountToWithdraw
        return account0Balance
    if accountNumber == 1:
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount!')
            return None

        if password != account1Password:
            print('Incorrect password')
            return None

        if amountToWithdraw > account1Balance:
            print('Insufficient funds')
            return None

        account1Balance = account1Balance - amountToWithdraw
        return account1Balance


newAccount(nAccounts, 'John Doe', 100, 'soup')
nAccounts = 1

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
        print('Show:')
        show()

    elif action == 'q':
        break

    else:
        print('Invalid input. Please try again')
