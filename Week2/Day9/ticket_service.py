tickets = []

def add_ticket(ticket):
    tickets.append(ticket)

def view_tickets():
    for ticket in tickets:
        ticket.display()


