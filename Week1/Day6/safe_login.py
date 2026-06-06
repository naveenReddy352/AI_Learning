try:
    age = int(input('Enter your age: '))
    print('Your age is:',age)
except ValueError:
    print('Please enter valid number for age.')
