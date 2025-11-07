
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



