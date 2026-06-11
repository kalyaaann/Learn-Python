#Modules in python 
#single py file 

#create a module mymodule.py file
#use mymodule.py 

import mymodule
mymodule.say_hello("Kalyan")
mymodule.say_bye("Ishan")

#import variables/specific part

from mymodule import record
print(record)
print(record['name'])

# packages : collection of modules/py files and __init__files


#libraries in python
#inbuilt libraries

import math 
a=25
print(math.sqrt(a))

#import specific function from libraries

from math import factorial
b=3
print(factorial(b))


#install new modules/libraries
#pip install <library_name>



