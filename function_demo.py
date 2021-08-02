'''#function
def add(x,y): #name of the function is "add" and x and y r variables.
    return x+y
x = 3
y = 4

z = add(x,y)
print("z =",z)

def substraction(a,b):
    return a - b
a = 234
b = 389
print(substraction(a,b))

def multiplication(x,y):
    return x*y
print(multiplication(x,y))

def division(a,b):
    return a/b
print(division(a,b))

def square(x):
    return x*x
print(square(20))




#LAMBDA FUNCTION:

adder = lambda x,y:x+y
print(adder(1,2))


import math
euclidian_distance = lambda x,y:math.sqrt((x**2)+(y**2))
print(euclidian_distance(3,4))


#map()
even_list = [2,4,6,8,10]
squared_even_list = map(lambda x: x*x,even_list)
print(list(squared_even_list))


#change from celsius to fahrenheit
c = [39.2, 36.5, 37.3, 38, 37.8]
fahrenheit_list = map(lambda x:(x*(9/5) + 32),c)
print(list(fahrenheit_list))'''


#lambdas in reduce()
from functools import reduce
even_list = [2,4,6,8,10]
'''product = reduce(lambda x,y:x*y,even_list)
print(product)
add = reduce(lambda x,y: x+y , even_list)
print(add)'''
squaring = map(lambda x: x*x ,even_list)
print(list(squaring))

add = reduce(lambda x,y: x+y , squaring)
print(add)
adding = reduce(lambda x,y: x+y,squaring)
print(adding)






