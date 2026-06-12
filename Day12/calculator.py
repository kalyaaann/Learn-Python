#Simple Project : Calculator

# Addition function
def addition(number1,number2):
     return number1 + number2 

# Subtraction Function
def subtraction(number1,number2):
     return number1 - number2 

# Multiplication function
def multiplication(number1,number2):
     return number1 * number2  

# Division Function 
def division(number1,number2):
     return number1 / number2 

# Average Function
def average(number1,number2):
     return (number1 + number2)/2  


#Taking the number input and operation input to perform from User

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("Please select a operation:\n " \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n") 

select = int(input("Enter the number of operation you want to perform : ")) 
