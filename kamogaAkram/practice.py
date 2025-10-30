class Car:
    def __init__(self):
        self.self = self
        self.make = "Toyota"
        self.model = "Corolla" 
    def display_info(self):
        return f"Car Make: {self.make}, Model: {self.model}" 

class bike:
    def __init__(self):
        self.self = self
        self.make = "bajaj"
        self.model = "1234"
    
    def display_info(self):
        return f"Bike Make: {self.make}, Model: {self.model}"
        
    
my_car = Car()
print(my_car.display_info())



my_bike = bike()
print(my_bike.display_info())


class Man:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        return(f'greetings my name is:{self.name}') 
    
class Woman(Man):
    def __init__(self,name,profession):
        super().__init__(name)
        self.profession = profession

    def introduce(self):
        return f'Hello, I am {self.name}, and I work as a {self.profession}.'
w = Woman('akram','engineer')                       
print(w.introduce())
m = Man('akram')        

print(m.introduce())    
    


