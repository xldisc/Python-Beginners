'''
a = 4
b = 2
c =9
average = (a + b + c)/3.0
print(average)

a1=5
b2=9
c3=2
average1 =(a1+b2+c3)/3
print(average1)
'''
def average(a, b, c):
    d = (a + b + c)/3.0
    #print(d)
    return d

o1 = average(3, 5, 1)
o2 = average(4, 2, 1)

print(o1)
print(o2)

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  