file = open('logs.txt','r')

print(file.name)
print(file.mode)
content = file.read()
print(content)

file.seek(0) #Because file.read() reads the whole file and moves the file cursor to the end. After that, for line in file: has nothing left to read.
for line in file:
    print(line,end='')

file.seek(0)
for line in file:
    if 'ERROR' in line:
        print(line,end='')

file.close()
