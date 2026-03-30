name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
print("{1} is learning {0}".format("python","Alince"))

print("{name} is {age} years old".format(name="Bob",age=25))
 
print(f"My name is {name} and I am {age} years old.")

x=20
y=65
print(f"The sum of {x} and {y} is {x+y}")

text="Python"
print(f"{text:>10}") #Right align
print(f"{text:<10}")  #left align
print(f"{text:^10}")  #centre align
