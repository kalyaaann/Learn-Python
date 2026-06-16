# #if statement
age = 23
if (age >=18):
    print("You are eligible to vote!")
# #elif statement
light = "red"
if(light == "red"):
    print("Stop!")
elif (light == "yellow"):
    print("Get Ready")
elif(light == "green"):
    print("Go!")
else :
    print("Light is off!")

# #grade distribution program using if elif and else statements. 
marks = int(input("Enter your marks : "))

if(marks>=90):
    print("you have achieved Grade A+")
elif(marks>= 80 and marks < 90):
     print("you have achieved Grade A")
elif(marks>= 70 and marks < 80):
     print("you have achieved Grade A")
elif(marks>= 60 and marks < 70):
     print("you have achieved Grade A")
elif(marks>= 50 and marks < 60):
     print("you have achieved Grade A")
elif(marks>= 40 and marks < 50):
     print("you have achieved Grade A")
else: 
    print("Failed!!")


#nesting : condition inside condition
n=int(input("Enter your age"))
have_lisence= True
if(n>18):
    if(have_lisence == True):
        print("You are eligible to drive ")
    else: 
        print("You don't have driving lisence to drive")
else: 
    print("You are not eligible to drive.")


#check if a number entered is odd or even
n= int(input("Enter a number"))

if (n%2==0):
    print("Even Number")
else:
    print("Odd Number")

#greatest number between a b and c

a=int(input("Enter first number : "))
b=int(input("Enter first number : "))
c=int(input("Enter first number : "))

if(a>=b and a>=c):
    print(a, "is greatest")
elif(b>=c):
    print(b, "is greatest")
else:
    print(c, "is the greatest")


#check whether a number is a multiple of 7 or not 
     
x= int(input("Enter a number"))
if(x%7 ==0 ):
    print(x, "is a multiple of 7.")
else:
    print(x, "is not a multiple of 7.")
