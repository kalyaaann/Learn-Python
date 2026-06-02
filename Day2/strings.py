string1 ="Kalyan"
string2= 'Prithvi Narayan Campus'
string3= """BSc CSIT, 4th semester"""

print(string1, string2, string3)

string ="My name is Kalyan.\n I am from Pokhara. \t I am a student."
print(string)

str1="Kalyan"
str2="Dhamala"
Fullname = str1+str2
print(Fullname)
print(len(Fullname))


#indexing : used for accessing the characters in string 


string= "Kalyan "
ch1= string[0]
ch2= string[1]
ch3= string[2]
ch4= string[3]
ch5= string[4]
ch6= string[5]
print(ch1)
print(ch2)
print(ch3)
print(ch4)
print(ch5)
print(ch6)

#slicing 


str= "Nepal Pokhara"
print(str[1:4]) #prints from 1st index to 3rd index
print(str[0:6]) #prints from 0th index to 5th index
print(str[6:14]) #prints from 6th index to 13th index
print(str[2:len(str)])  #prints from 2nd index to index of length of string(last)
print(str[2:])  #prints from 2nd  index to last index
print(str[:5]) #prints from 1st index to 4th index

slice="apple"
print(slice[-5:-1]) #negative slicing

#string functions
 
str="hi, I am learning Python"
print(str.endswith("thon")) #checks the end of the strings. returns true if matched and returns false if not matched.
print(str.endswith("ok"))
print(str.capitalize()) #capitalizes the first character of the string. 

print(str.replace("Python", "oop")) #replaces the old strings with new one.

print(str.find("a")) #returns the index of first 'a' occured in the string 

print(str.count('n')) #returns how many times 'n' is occured on the given string str.


#WAP to input user's name and print its length 

name= input("Enter your name: ")
print(len(name))

#WAP to find the occurance of 'S' in a string 

string= input("Enter a string :")
print(string.count('$'))