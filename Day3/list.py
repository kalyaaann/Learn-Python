#list in python 

marks=[14,24,53,45.5,89.5,95]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(marks[:4])
print(marks[0:])
print(len(marks))

#list can store data of any type 

record=['Kalyan',4, 15, "Pokhara"]
print(record)

#Lists are mutable in python

student=["Ram",97,19,"Nepal"]
print(student)
student[0]='Hari'
print(student)

#list methods.

list=[2,4,3,1,5]
list.append(0) #adds the element on the last of the list
print(list)
list.sort() #sorts the list in ascending order
print(list)
list.sort(reverse=True) #sorts list in descending order
print(list)
list.reverse()  #reverses the given list...last value goes first and first goes last
print(list)
list.insert(5,6) #inserts the value 6 at 5th index
print(list)
list.remove(4) #removes the first occurance of 4 from the list
print(list)
list.pop(3) #removes the element on index 3
print(list)