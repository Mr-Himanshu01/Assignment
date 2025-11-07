# Task 1: Basic Mathematical Operations
""" This program do the Basic Mathematical Operations like 
Addition, Subtraction, Multiplication and Division.
- Here User have to give inputs of the 2 number on which he wants to do the Mathematical Operations.
- Example : Inputs,
            Enter the first number: x
            Enter the second number: y

            Result,
            Addition: x+y
            Subtraction: x-y
            Multiplication: x*y
            Division: x/y

"""
            

First_Number = int(input("Enter the first number:"))
Second_Number = int(input("Enter the second number:"))

# do the required basic mathematical operations with given input

Addition = First_Number + Second_Number

Subtraction = First_Number - Second_Number

Multiplication = First_Number * Second_Number

Division = First_Number / Second_Number

print("Addition:", Addition)

print("Subtraction:", Subtraction)

print("Multiplication:", Multiplication)

print("Division:", Division)


# Task 2: Greet User With his Name
""" This program do Greet to the User like 
Hello, User Name! Welcome to the python program.
- Here User have to give inputs of the first Name and last Name. 
- Example:  Inputs, 
            Enter your first name: Himanshu
            Enter your last name: Girase
            
            Result,
            Hello, Himanshu Girase! Welcome to the python program          
"""

First_Name = input("Enter your first name: ")
Last_Name = input("Enter your last name: ")

# do the Concatenation with the first name and last name into a full name with given input

Full_Name = First_Name +" " + Last_Name

print("Hello, ", Full_Name, "! ", "Welcome to the python program", sep = "")


