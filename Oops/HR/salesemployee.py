class salesEmployee:
    def __init__(self, Firstname, lastname,email, contactno , workingDays,  dailywages, providentfund=500, insentive = 7000, target = 500, commission = 0.02):
        self.Firstname = Firstname
        self.lastname = lastname
        self.email = email
        self.contactno = contactno
        self.workingDays = workingDays
        self.dailywages = dailywages    
        self.providentfund = providentfund
        self.insentive = insentive
        self.target = target
        self.commission = commission
    def compute_salary(self, total_sales):
        basesalary = self.workingDays * self.dailywages
        tax = 0.18 * basesalary
        self.totalsalary = basesalary - tax - self.providentfund
        self.totalsalary += self.commission * total_sales
        if total_sales >= self.target:
            self.totalsalary += self.insentive
        print(f"Total Salary: {self.totalsalary}")

    def display_info(self):
        print(f"Name: {self.Firstname} {self.lastname}")
        print(f"Email: {self.email}")
        print(f"Contact No: {self.contactno}")
        print(f"Working Days: {self.workingDays}")
        print(f"Daily Wages: {self.dailywages}")
        print(f"Provident Fund: {self.providentfund}")
        print(f"Insentive: {self.insentive}")
        print(f"Target: {self.target}")
emp1 = salesEmployee("John", "Doe", "john.doe@example.com", "1234567890", 50000, 22, 200, 5000)
total_sales = int(input("Enter total sales made by the employee: "))
emp1.compute_salary(total_sales)
emp1.display_info()