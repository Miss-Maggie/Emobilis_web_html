#list datastructures
#list is ordered
#list has indexes
#list is changeable
fruits = ["apple", "banana", "cherry"]
fruits.sort()
fruits.append("orange")
print(fruits)
print(f"I like eating {fruits[0]} and {fruits[3]}")



#tuple datastructures
#tuples are ordered
#you cannot assign a tuple
#tuple is unchangeable
cars=("bmw", "subaru", "nissan", "mercedes")
print(cars)
print(f"{cars[0]} are manufactured in Germany")

#set datastructures
#sets are unordered
#set does not allow duplicate
majina={"Eric", "Maggie", "Ivy", "Njeri"}
majina.add("Maria")
print(majina)


#dictionary datastructures
staff={"Name": "Magdaline", "Age": "25", "Gender": "Female"}
print(staff)
print(f"staff name is {staff['Name']}")

