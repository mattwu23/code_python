# program goal : build a simple python program that can add, subtract, multiply, divide two numbers

#Functional Decomp
# obtain a way to get two numbers
# obtain a way to choose either add, subtract, multiply, divide
# do the wanted calculation with the given 2 numbers
# output calculation/result

print ("Welcome to our calculator app!")

# 1. obtain a way to get 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input ("Enter the second number: "))

#obtain a way to choose either add, subtract, mutiply, divide
choice = input("Choose either add, subtract, multiply or divide: ")

# do the wanted calculation with the given 2 numbers
# out put the calculation/result

if choice == "add":
    print(num1 + num2)
elif choice == "subtract":
    print(num1 - num2)
elif choice == "multiply":
    print(num1*num2)
elif choice == "divide":
    print(num1/num2)