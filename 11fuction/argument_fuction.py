
#Positional Arguments
def add(a, b):
    return a + b

print(add(5, 3)) 

#Default Arguments

def greet(name="Guest"):
 return f"Hello,{name}!"

print(greet())

#Keyword Arguments
def student(name,age):
   print(f"Name: {name} ,Age:{age}")
student(age=20,name="aman")