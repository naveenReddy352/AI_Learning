file = open('logs2.txt','w')
file.write('INFO: This is info message \n')

file = open('logs2.txt','a')
file.write('ERROR: This is error message') 


file.close()

#opened the file with mode 'w', which means “write and truncate.” That clears the file first, 
# then writes your new text.

#If you want to add text instead, use append mode 'a'