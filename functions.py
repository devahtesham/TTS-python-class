# # function declaration
# if False:
#     my_name = "ahtesham"
# fname = "Techzone"
# lname = "Institute"
# # print(fname+" "+lname)
# print(f"My Institiue name is {10+10} and {lname}")





# fname = "techzone"
# lname = "institute"
# std1 = "ali"
# std2 = "aslam"
# std3 = "kasim"
# std4 = "ahmed"
# std5 = "hassan"
# def myFunc(name,*name2): # parameter
#     # body of a function 
#     print(name)
#     print(name2)
     
# myFunc(fname,lname,std1,std2,std3,std4,std5) # arguements
# calling a function 
# def newFunc(a,b=20):
#     print(a,b)
    
# x=int(input("Enter your number :  "))
# for i in range(x):
#     x =   x + i
# print(x) 

# def sumOfSeries(y):
#     for i in range(y):
#         y =   y + i
#     return y

# umamima = sumOfSeries(x)
# print(umamima)

# def func():
#     name= "ahtesham"
#     id= 10
#     edu= "BS"
# func()

# ============= OOP ( Object Oriented Programming ) IN PYTHON ========
class Car:
    def __init__(self, name,color,make):
        self.name = name
        self.color = color
        self.make = make
    def moveFast(self):
        print(f"{self.name} is moving fast")
    
    def flyingGear(self):
        print(f"{self.name} has flying option and its color is {self.color}")

car1 = Car("Civic","Black","Honda")
car2 = Car("city","red","toyota")
# print(car1.name)
car1.moveFast()
car2.moveFast()