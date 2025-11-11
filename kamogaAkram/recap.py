class Student:
    def great(self):
        print("i am a student.")

class ClassRep(Student):
    def great(self):
        print(" i am a Class Rep,taking attendence!")

class GuildPresident(Student):
    def great(self):        print(" i am the Guild President - lets improve our campus")

people = [Student(), ClassRep(), GuildPresident()]
for person in people:
    person.great()