class Ticket:
    def __init__(self,id,issue,severity):
        self.id = id
        self.issue = issue
        self.severity = severity
    
    def display(self):
        print("__________")
        print("ID: ",self.id)
        print("Issue: ",self.issue)
        print("Severity: ",self.severity)


tickets = []

tickets.append(Ticket(1,"JVM Error","High"))
tickets.append(Ticket(2,"Login Failure","Medium"))

for ticket in tickets:
    ticket.display()
