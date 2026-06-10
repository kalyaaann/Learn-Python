try:
    a=int(input("Enter a number : "))
    b=7/a
    print(b)
except:
    print("Error in input. Please enter correct number")

list=[1,2,3,4,5]
for i in list:
    print(i)


#finally block
try:
    a=int(input("Enter a number : "))
    b=7/a
    print(b)
except:
    print("Error in input. Please enter correct number")

finally:
    print("This code will always execute.")

