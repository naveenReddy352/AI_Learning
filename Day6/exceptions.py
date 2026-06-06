#number = int(input("Enter a number: "))

#print(number)

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception:
    print("Enter Valid Input")
else:
    print("Input is valid.")
finally:
    print("This finally block will always be executed.")


#Else clause is executed if no exceptions are raised in the try block. It is optional and can be used 
# to perform actions that should only occur if the try block succeeds without any exceptions.
#Finally clause is executed regardless of whether an exception was raised or not. 
# It is typically used for cleanup actions, such as closing files or releasing resources, 
# that should always be performed regardless of the outcome of the try block.
