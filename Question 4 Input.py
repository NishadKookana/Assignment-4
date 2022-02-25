#Question 4

class Student:
    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum
    def __del__(self):
        print("Destructor called,The object is destroyed.")

p1=Student("Sarthak",19)
print(p1.name)
print(p1.rollnum)
