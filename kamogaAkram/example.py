class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Using encapsulation
account = BankAccount()
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())




class Person:
    def walk(self):
        print("Person is walking.")

class Employee(Person):
    def work(self):
        print("Employee is working.")

# Using inheritance
emp = Employee()
emp.walk()
emp.work()


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stopped.")

class Car(Vehicle):
    def start(self):
        print("Car engine started.")

# Using abstraction
my_car = Car()
my_car.start()
my_car.stop()
