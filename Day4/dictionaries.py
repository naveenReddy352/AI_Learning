student = {'name':'John','age':25,'courses':['Maths','English']} 
#This is a dictionary. A dictionary is a collection of key-value pairs. 
# Each key is separated from its value by a colon (:), and the items are separated by commas. 
# The whole thing is enclosed in curly braces {}. 
# The keys must be unique and immutable (like strings, numbers, or tuples), 
# while the values can be of any data type and can be duplicated.

student['phone'] = '123-456' 
student['name'] = 'Jane' 
student.update({'name':'John','age':26,'phone':'987-654'})
del student['phone']
age = student.pop('age') 

print(age)
print(student)
print(student['name'])
print(student['courses'])
print(len(student))
print(student.items())

for key,value in student.items():
    print(key,value)
