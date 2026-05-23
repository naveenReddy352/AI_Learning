with open('logs.txt','r') as file:
    for line in file:
        if 'WARNING' in line:
            print(line,end='')

file.close()
