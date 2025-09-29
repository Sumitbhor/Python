class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}\nPosition: {self.position}\nSalary: ${self.salary}")
        
emp1 = Employee("Alice", "Developer", 80000)
emp1.display_info()

emp2 = Employee("Bob", "Manager", 95000)
emp2.display_info()