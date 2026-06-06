from ticket import Ticket #importing the Ticket class from the ticket module
from ticket_service import add_ticket, view_tickets 
#importing the add_ticket and view_tickets functions from the ticket_service module
from utils import print_header #importing the print_header function from the utils module

print_header() #calling the print_header function to display the header of the support system

#ticket1 = Ticket("JVM Error","High") #creating an instance of the Ticket class
#ticket2 = Ticket("Login Failure","Medium")

#add_ticket(ticket1) #adding the ticket to the ticket service
#add_ticket(ticket2)

while True:
    issue = input("Enter the issue: ")
    if issue.lower() == "exit":
        break

    severity = input("Enter the severity (Low/Medium/High): ")
    ticket = Ticket(issue,severity) #creating a new ticket with the user input
    add_ticket(ticket)


view_tickets() #calling the view_tickets function to display all tickets

