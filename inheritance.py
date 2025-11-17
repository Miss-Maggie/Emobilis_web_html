class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello my name is {self.name}!")

class Teacher(Person):
    def __init__(self, name, subject):  #inherits from person class
        super().__init__(name)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying {self.grade}")

t1=Teacher("Miss Maggie", "Python Programming")
t1.teach()

s1=Student("Ignatius", "Grade 10")
s1.study()