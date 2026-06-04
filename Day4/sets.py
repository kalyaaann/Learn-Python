set0={ 1,2,3,4}
print(set0)
print(type(set0))

set1={1,2,3,4,2,1,3,"hello","world","hello",5}
print(set1)   #prints the elements in random order
print(len(set1)) #counts the elements and skips the repeated values.
print(len(set0))

#empty set
empset = set()
print(type(empset))

#set methods
empset.add(49) #adds 49 to the set
empset.add(200)
print(empset)
empset.remove(200) #removes 200 from set
print(empset)
empset.add(1)
empset.add(10)
empset.add(20)
print(empset)
empset.pop() #removes the value random
print(empset)
empset.clear() #clears the list
print(empset)

#union and intersection 
sett1={1,2,3,4,5}
sett2={2,4,6,8,10}
print(sett1.union(sett2)) #gives the union of two sets
print(sett1.intersection(sett2)) #gives the intersection of two sets

