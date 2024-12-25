from Bank import *

oBank = Bank()

joesAccountNumber = oBank.createAccount('Joe', 100, 'password')
print('Account number for Joe is:', joesAccountNumber)

marysAccountNumber = oBank.createAccount('Mary', 200, 'password')
print('Account number for Mary is:', marysAccountNumber)

while True:
    print()
    print('To get and account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To open a new account, press o')
    print('To make a withdrawal, press w')
    print('To show all accounts, press s')
    print('To quit, press q')
    print()

    action = input('What do you want to do?')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        oBank.getBalance()
    
    elif action == 'c':
        oBank.closeAccount()

    elif action == 'd':
        oBank.deposit()

    elif action == 'o':
        oBank.openAccount()

    elif action == 'w':
        oBank.withdraw()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    else:
        print('Invalid action. Please try again.')

print('Done')
