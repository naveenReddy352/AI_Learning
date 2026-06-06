def hello():
    return 'Hello!!'

hello() # This will not print anything because we are not using print function to display the output of hello() function.
print(hello())
print(hello().upper())

def greeting(greet,name):
    return greet + ' '+name
print(greeting('Hi','Nav'))
