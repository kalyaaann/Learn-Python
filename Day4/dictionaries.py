dict={
    "Name":"Kalyan",
    "Course":"Bsc CSIT",
    "GPA":3.60,
    "is_student":True,
    "age":19,
    "list":["python","html","css","javascript",],
    "tuple":('pkr','ktm','npl',),
    }
# print(dict)
# print(dict["Name"])
# print(dict["list"])

#null dictionary

# null_dict={}
# null_dict["Name"]="Kalyan"
# print(null_dict)
# null_dict["address"]="Pokhara"
# print(null_dict)
# print("The dictionaries are mutable in python")


#nested dictionaries

student={
    "name":"KALYAN",
    "MARKS":{
        "1ST SEM":3.52,
        "2ND SEM": 3.60,
    },
    "Skills":{
        "programming":"python",
        "designing":"Figma",
    },

    }
print(student)

#dictionary methods. 
print(student.keys()) #returns all the keys of the dictionaries
print(student.values()) #returns all the values of the dictionaries. 
print(student.items()) #returns all the key value pairs as tuples of the dictionaries
print(student.get("name")) #returns the value of name key from student dictionary
print(student.update({"age":19,})) #adds to the existing dictionary
print(student)