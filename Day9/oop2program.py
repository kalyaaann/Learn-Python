#pq1
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("name =", self.name)
        print("age =", self.age)
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "60,000")


engg1 = Engineer("Balen Shah", 40)
engg1.showDetails()

#pq2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius


c1 = Circle(5)
print(c1.area())
print(c1.perimeter())

#pq3

class Order:
    def __init__(self,item,price):
        self.item=item 
        self.price =price 
    def __gt__(self,ord2):
        return self.price > ord2.price
    
ord1=Order("Keyboard",2000)
ord2= Order("Mouse",800)

print(ord1>ord2)