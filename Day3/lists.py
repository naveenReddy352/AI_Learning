courses = ['Maths','Science','Tech']

print(courses)
print(len(courses))
print(courses[0])
print(courses[2])
print(courses[-1]) #Negative indexing starts from the end of the list. -1 is the last element, -2 is the second last element and so on.
print(courses[0:2]) #2 is exclusive
courses.append('History')
print(courses)
courses.insert(0,'Geography')
print(courses)
courses.extend(['Art','Music']) #This will add the elements of the list ['Art','Music'] to the end of the courses list. It is different from append() method which adds the entire list as a single element to the end of the courses list.
print(courses)
courses.remove('Tech')
print(courses)
courses.pop() #This will remove the last element of the list and return it. If we want to remove a specific element from the list, we can use the remove() method.
print(courses)
courses.reverse()
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)
print(min(courses))
print(max(courses))
print(courses.index('Maths'))
print('Maths' in courses)

course_str = ', '.join(courses) #This will join the elements of the courses list into a single string with ', ' as the separator. The join() method is a string method that takes an iterable (like a list) and returns a string that is the concatenation of the elements of the iterable, separated by the string on which the method is called.
print(course_str)