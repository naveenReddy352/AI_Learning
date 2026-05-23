tickets = []

ticket1 = {'id':101,'Issue':'JVM Error',
          'details':{'severity':'High','status':'open'}
          }

print(ticket1)
print(ticket1['id'])
print(ticket1['details'])
print(ticket1['details']['severity'])

ticket2  = {'id':102,'Issue':'Name Null','severity':'low'}

tickets.append(ticket1)
tickets.append(ticket2)

for ticket in tickets:
    print(ticket['id'],ticket['Issue'])
    print(ticket)

