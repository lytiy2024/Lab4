# change the value for a different result
num = 7

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)


choice = int(input(colored(color='blue', attrs=['underline'], text='Оберіть операцію :')))
return_selection = int(input(colored(color='blue', attrs=['underline'], text='Введіть суму :')))

if choice == 1:
    z_pdv()
elif choice == 2:
    bez_pdv()
elif choice == 3:
    pdv()
elif choice > 3:
    print('невірно.')
