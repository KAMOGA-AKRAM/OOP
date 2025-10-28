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



