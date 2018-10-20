def add(x,y):
    """This function adds 2 number"""
    return x+y


def subtract(x,y):
    """This function subtsract 2 number"""
    return x-y


def multiply(x,y):
    """This function multiply 2 number"""
    return x*y


def divide(x,y):
    """This function divide 2 number"""
    return x/y


def power(x,y):
    """This gives power"""
    return pow(x,y)
print("Select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
choice=input("Enter choice(1/2/3/4/5):")

num1=int(input("Enter first number"))
num2=int(input("Enter the second number"))

if chocie =='1':
    print(num1,"+", num2,"=", add(num1,num2))
elif chocie == '2':
     print(num1,"-", num2,"=", substract(num1,num2))
elif chocie == '3':
     print(num1,"x", num2,"=", multiply(num1,num2))
elif chocie == '4':
     print(num1,"/", num2,"=", divide(num1,num2))
elif chocie == '5':
     print(num1,"^", num2,"=", power(num1,num2))
else:
    print("Invalid input")
