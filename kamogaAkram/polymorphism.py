# Parent class
class Employee:
    def __init__(self, name):
        self.name = name

    



class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


# Testing polymorphism
employees = [
    FullTimeEmployee("AKRAM", 30000),
    PartTimeEmployee("Jane", 20, 80),
    Intern("Mike", 200)
]

for emp in employees:
    print(f"{emp.name}'s salary is: ${emp.calculate_salary()}")





# Parent class
class PoliticalParty:
    def __init__(self, name, slogan):
        self.name = name
        self.slogan = slogan

    def display_info(self):
        print(f"Party: {self.name}")
        print(f"Slogan: {self.slogan}")



class PartyA(PoliticalParty):
    def __init__(self, candidate_name):
        super().__init__("Unity Party", "Together We Rise")
        self.candidate_name = candidate_name


class PartyB(PoliticalParty):
    def __init__(self, candidate_name):
        super().__init__("Freedom Alliance", "Power to the People")
        self.candidate_name = candidate_name


class PartyC(PoliticalParty):
    def __init__(self, candidate_name):
        super().__init__("Green Future", "For a Sustainable Tomorrow")
        self.candidate_name = candidate_name



candidate1 = PartyA("Alice")
candidate2 = PartyB("Bob")
candidate3 = PartyC("Carol")


for candidate in [candidate1, candidate2, candidate3]:
    print(f"\nCandidate: {candidate.candidate_name}")
    candidate.display_info()







        