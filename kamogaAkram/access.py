class student:
    def __init__(self,name,):
        self.name = name         #public 
        self._gpa = 3.5           #protected
        self.__password = '1234'     # private
    
    
    
s1 = student('akram')
print (s1.name)
print(s1._gpa)
print(s1._student__password)


