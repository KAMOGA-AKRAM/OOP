class Employee:
    def __init__(self,get_salary):
        self.get_salary = get_salary

class FullTimeEmployee(Employee):
    def __init__(self, get_salary):
        super().__init__(get_salary)

class PartTimeEmployee(Employee):
    def __init__(self, get_salary):
        super().__init__(get_salary)





        