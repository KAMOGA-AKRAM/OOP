class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        return(f'greetings my name is:{self.name}')


class Student(Person):
    def __init__(self,name,programme,year):
        super().__init__(name)
        self.programme = programme
        self.year = year
    


class Lecturer(Person):
    def __init__(self,name,department):
        super().__init__(name)
        self.department = department
        

p = Person('AKRAM')
s = Student('paul','computer science',2)
l = Lecturer('bomboclat','IT')

print(p.introduce())
print(s.introduce())
print(l.introduce())

