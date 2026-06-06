
class Ticket:
    def __init__(self,issue,severity):# The __init__ method is a constructor method in Python 
                             # that is called when an object is created. It initializes the object's attributes.
        self.issue = issue #The self parameter refers to the current object or instance of the class being created.
        self.severity = severity # The severity attribute stores the severity level of the ticket.
    
    def display(self):# The display method is defined to print the issue and severity of the ticket.
        print("Issue: ",self.issue)
        print("Severity: ",self.severity)

ticket1 = Ticket("JVM Error", "High") # Create an instance of the Ticket class

print(ticket1.issue)
print(ticket1.severity)

ticket1.display() # Call the display method to print the issue and severity of the ticket

print("\n") # Print a newline for better readability

ticket2 = Ticket("Login Failure","Medium")
ticket2.display() # Call the display method to print the issue and severity of the second ticket

tickets = [] # Create an empty list to store multiple ticket instances
tickets.append(ticket1) # Add the first ticket to the list
tickets.append(ticket2) # Add the second ticket to the list

for ticket in tickets: # Iterate through the list of tickets and call the display method for each ticket
    ticket.display()
    print("\n") # Print a newline for better readability between tickets

