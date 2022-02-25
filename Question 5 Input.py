#Question 5

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

p1=employee("Mehak",40000)
p2=employee("Ashok",50000)
p3=employee("Viren",60000)


# Part A

#updating salary of Mehak to 70000

p1.salary=70000
print("The updated salary of Mehak is-",p1.salary)


# Part B

#deleting the record of Viren

del p1
print("The record of Viren has been successfully deleted-")


