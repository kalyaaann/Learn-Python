"""Create a student class that takes name and marks of 3 subjects
as arguments in constructor. Then create a method to calculate average"""

class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def calc_avg(self):
        sum=0
        for value in self.marks:
            sum+=value
        print("hi ",self.name, ". Your average marks is ", sum/3)


s1=Student("Kalyan Dhamala",[99,92,82])
s1.calc_avg()


"""Create Account class with 2 attributes -balance and account_no.
Create methods for debit, credit and printing balance"""
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc    
    #debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount ,"was debited from", self.account_no)
        print("Total Balance :",self.totalbalance())
    #credit method
    def credit(self,amount):
        self.balance+= amount
        print("Rs.",amount ,"was credited from", self.account_no)
        print("Total Balance :",self.totalbalance())
    #print balance method
    def totalbalance(self):
        return self.balance
    
acc1=Account(10000,123456789)
print(acc1.balance)
print(acc1.account_no)
acc1.credit(1000)
acc1.debit(2000)