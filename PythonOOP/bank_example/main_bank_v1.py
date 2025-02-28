from Account import *

oJoesAccount = Account('Joe', 100, 'Joespassword')
print('Created account for Joe')
oMarysAccount = Account('Mary', 500, 'Maryspassword')
print('Created account for Mary')
oJoesAccount.show()
oMarysAccount.show()
print()


print('calling methods of the two accounts')
oJoesAccount.deposit(50, 'Joespassword')
oMarysAccount.withdraw(345, 'Maryspassword')
oMarysAccount.deposit(100, 'Maryspassword')

oJoesAccount.show()
oMarysAccount.show()
