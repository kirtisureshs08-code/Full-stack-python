class Employee:
    def __init__(self,name,emp_id,salary):
        self.name= name
        self.emp_id=emp_id
        self.salary=salary
    def show(self):
        print(self.name)
        print(self.emp_id)
        print(self.salary)
e=Employee("kirtika",102,30000)
e.show()            
