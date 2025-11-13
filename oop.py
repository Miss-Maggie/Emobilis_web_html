# define a class
class Student:
    # define a constructor
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    # define a method
    def display(self):
        print(f"Name:{self.name} Age:{self.age} Score:{self.score}")

    # define a method to check if student pass
    def check_pass(self):
        return self.score >= 90

# create objects
s1=Student("James",35,90)
s2=Student("Jane",25,80)

#use methods
s1.display()
s2.display()

print(f"{s1.name} passed: {s1.check_pass()}")
print(f"{s2.name} passed: {s2.check_pass()}")


