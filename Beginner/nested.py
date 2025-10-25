class Company:
    class Employee:
        def __init__(self , name , position):
            self.name = name 
            self.position = position
        
        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name ):
        self.company_name = company_name
        self.employees = []
    
    def add_employee(self , name , position):
        new_employee = self.Employee(name , position)
        self.employees.append(new_employee)

    def list_employee(self):
        return [employee.get_details() for employee in self.employees] 


company1 = Company("Krust Krab")
company2 = Company("Chumb")

company1.add_employee("John" , "Manager")
company1.add_employee("Bob" , "Cook")
company1.add_employee("Pop" , "Cashier")

company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", " Assi Manager")

for employee in company2.list_employee():
    print(employee)
