# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))

def is_power (n):
    print(n)
    if n == 1:
        return 'Є степенем 5'
    if n < 1:
        return 'Не є степенем 5'
    return is_power (n/5)

def pdv():
    """Функція рахує суму з ПДВ та без ПДВ"""
    x2 = return_selection * 6
    y2 = return_selection * 6 - return_selection
    print('Сума ПДВ ->', return_selection)
    print('Сума з ПДВ ->', x2, 'грн')
    print('Сума без ПДВ ->', y2, 'грн')
