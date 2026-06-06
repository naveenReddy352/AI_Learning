class Employee:
    def __init__(self,name,role):
        self.name = name
        self.role = role
    
    def display(self):
        print("____________")
        print("Name: ",self.name)
        print("Role: ",self.role)


employees = []
employees.append(Employee("Naveen","Developer"))
employees.append(Employee("Kumar","Tester"))

for employee in employees:
    employee.display()


