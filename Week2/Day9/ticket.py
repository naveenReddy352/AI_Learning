class Ticket:
    def __init__(self,issue,severity):
        self.issue = issue
        self.severity = severity
    
    def display(self):
        print("Issue: ",self.issue)
        print("Severity: ",self.severity)


