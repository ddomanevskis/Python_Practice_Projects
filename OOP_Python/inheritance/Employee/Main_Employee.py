from EmployeeManagerInheritance import *

oEmployee1 = Employee('Joe Schmoe', 'Pizza Maker', 16)
oEmployee2 = Employee('Chris Smith', 'Cashier', 14)
oManager = Manager('Sue Jones', 'Pizza Restaraunt Manager', 55000, [oEmployee1, oEmployee2])

print('Emloyee name:', oEmployee1.getName())
print('Employee salary:', '{:,.2f}'.format(oEmployee1.payPerYear()))
print('Emloyee name:', oEmployee2.getName())
print('Employee salary:', '{:,.2f}'.format(oEmployee2.payPerYear()))
print()

managerName = oManager.getName()
print('Manager name: ', managerName)

print('Manager salary:', '{:,.2f}'.format(oManager.payPerYear(True)))
print(managerName, '(' + oManager.getTitle() + ')', 'direct reports: ')
reportsList = oManager.getReports()
for oEmployee in reportsList:
    print(' ', oEmployee.getName(),
          '(' + oEmployee.getTitle() + ')')
