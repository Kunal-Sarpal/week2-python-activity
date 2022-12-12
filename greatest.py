def greater(a,b,c):
    if a>b:
        return a
    else:
        return b
num1 = int(input("Enter first number"))
num2 = int(input("enter Second number "))
bigger = greater(num1, num2)
print(f"{bigger} is greater") 
