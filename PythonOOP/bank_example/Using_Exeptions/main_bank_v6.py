from Bank import *

oBank = Bank('9 to 5', '123 Main Str', '(650) 555-1212')

while True:
    print()
    print('To get an account balance, press b')
    print('to open an account, press o')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To close an account, press c')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What would you like to do? ')
    action = action.lower()
    action = action[0]
    print()

    try:
        if action == 'b':
            oBank.balance()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'd':
            oBank.deposit()
        elif action == 'i':
            oBank.getInfo()
        elif action == 'o':
            oBank.openAccount()
        elif action == 's':
            oBank.show()
        elif action == 'w':
            oBank.withdraw()
        elif action == 'q':
            break
    except AbortTransaction as error:
        print(error)

print('Done')