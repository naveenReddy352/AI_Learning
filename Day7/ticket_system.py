tickets = []

def add_ticket():
    issue = input('Enter the issue: ')
    severity = input('Enter the severity (low, medium, high): ')

    ticket = {'id': len(tickets)+1,
              'issue': issue,
              'severity': severity}

    tickets.append(ticket)

    print('Ticket added successfully!')

def view_tickets():
    if len(tickets) == 0:
        print('No tickets found')
        return

    for ticket in tickets:
        print('--------------------')
        print('Issue:', ticket['issue'])
        print('Severity:', ticket['severity'])

def save_tickets():
    try:
        with open('tickets.txt', 'w') as file:
            for ticket in tickets:
                file.write(f"Issue: {ticket['issue']}, Severity: {ticket['severity']}\n")

        print('Tickets saved successfully!')
    except Exception as e:
        print('Error saving tickets:', str(e))

def search_tickets():
    keyword = input('Enter keyword to search:')
    for ticket in tickets:
        if keyword.lower() in ticket['issue'].lower():
            print(ticket)

while True:
    print('\nSupport Ticket System')
    print('1. Add Ticket')
    print('2. View Tickets')
    print('3. Save Tickets')
    print('4. Search Tickets')
    print('5. Exit')

    try:
        choice = input('Enter your choice: ')
        if choice == '1':
            add_ticket()
        elif choice == '2':
            view_tickets()
        elif choice == '3':
            save_tickets()
        elif choice == '4':
            search_tickets()
        elif choice == '5':
            print('Exiting Support System.')
            break
        else:
            print('Invalid choice. Please try again.')
    except Exception as e:
        print('An error occurred:', str(e))
