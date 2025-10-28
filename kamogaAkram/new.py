class A:
    def greet(self):
        return "Hello from class A"
    
class B(A):
    def greet(self):
        return "Hello from class B"

class C(A):
    def greet(self):
        return "Hello from class C"
    
class D(C,B):
    pass
    
o = D()
print(o.greet())


