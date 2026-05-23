student = {'name':'John','age':25,'courses':['Maths','English']}

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
