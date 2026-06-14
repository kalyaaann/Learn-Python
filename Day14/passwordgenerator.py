import random
import string

def randompass(length):

    letters=string.ascii_letters
    digits=string.digits
    symbols=string.punctuation
    characterall=letters+digits+symbols

    password = ""

    for i in range(length):
        password += random.choice(characterall)
    return password

length= int(input("Enter the length of the password : "))
print("The random password generated is :", randompass(length))
