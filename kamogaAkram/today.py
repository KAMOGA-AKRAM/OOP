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

    def introduce(self):
        return f'Hello, I am {self.name}, a {self.year} year student of {self.programme}.'


class Lecturer(Person):
    def __init__(self,name,department):
        super().__init__(name)
        self.department = department

    def introduce(self):
        return f'Hello, I am {self.name}, a lecturer in the {self.department} department.'

p = Person('AKRAM')
s = Student('paul','computer science',2)
l = Lecturer('bomboclat','IT')

print(p.introduce())
print(s.introduce())
print(l.introduce())

