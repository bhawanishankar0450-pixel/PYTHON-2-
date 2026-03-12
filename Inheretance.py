class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):  
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Salary: {self.salary}")


class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def display_manager(self):
        print("\n--- Manager Details ---") 
        self.display_person()
        self.display_employee()
        print(f"Department: {self.department}")


manager1 = Manager("ABC", 35, "1000", 95000, "IT")
manager1.display_manager() 