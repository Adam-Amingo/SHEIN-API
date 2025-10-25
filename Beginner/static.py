class Employee:
    def __init__(self, name , position):
        self.name = name 
        self.postion = position

    def get_info(self):
        return f"{self.name} = {self.postion}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager" , "Cook" , "Casheir", "Janitor"]
        return position in valid_positions
    
empoyee1 = Employee("Eugene" , "Manager")
empoyee2 = Employee("Skibz" , "Casheir")
empoyee3 = Employee("Bob" , "Cook")

    
print(Employee.is_valid_position("Cook"))
print(empoyee1.get_info())
print(empoyee2.get_info())
print(empoyee3.get_info())