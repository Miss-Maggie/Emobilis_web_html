def myfunction():
    print("Hello World")
myfunction()
myfunction()
myfunction()

# function with parameters
def students(name, age, gender):
    print(f"The student name is {name}")
    print(f"The student age is {age}")
    print(f"The student gender is {gender}")
students("Magdaline", 22,"Female")
students("Ignatius", 22,"Male")

# function with return value
def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(5,10)
print(result)