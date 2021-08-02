'''Tuples are identical to lists in all respects except for the
following properties:
1. Tuples are defined by enclosing the elements in parenthesis () instead
of [].
2. Tuples are immutable(unable to change)'''

# Defining tuple
colours = ("red","blue","green","yellow")
print(type(colours))
for i in colours:
    print(i)

print(colours[2])
print(colours[:3])

# What are the benefits of using tuples instead of lists in python?
colours = ("red","blue","green","yellow") #Tuple packing
(c1,c2,c3,c4) = colours #Tuple unpacking
print(c3)

(c1,c2) = colours
print(student)

colour_1 = ("red",("blue","green"),"yellow")
print(type(colour_1))
print(colour_1)
print(colour_1[1][0])

#print(student_1[2][0])
