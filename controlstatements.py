#if // else statement
num=int(input("Enter a number:"))

if num%2==0:
    print(f"{num} is an Even Number")
else:
    print(f"{num} is an Odd Number")

#if elif else statemment
marks=int(input("Enter marks:"))
if marks>=80 and marks<=100:
    print(f"{marks} is an A")
elif marks>=70 and marks<=80:
    print(f"{marks} is an B")
elif marks>=60 and marks<=70:
    print(f"{marks} is C")
elif marks>=50 and marks<=60:
    print(f"{marks} is D")
elif marks>=40 and marks<=50:
    print(f"{marks} is E")
else:
    print(f"{marks} is F")