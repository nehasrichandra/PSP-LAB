'''import arithmetic_functions
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
sum = arithmetic_functions.add(x,y)

print("The sum of x and y is:%d"%(sum))
print("The sum of x and y is:",sum)

diff = arithmetic_functions.sub(x,y)
print("The difference of x and y is:%d"%(diff))

multi = arithmetic_functions.mul(x,y)
print("The product of x and y is:%d"%(multi))

div = arithmetic_functions.div(x,y)
print("The div of x and y is:%d"%(div))'''


#To find numerical aperture
import optical_fiber
D = float(input("Enter the diameter: "))
L = float(input("Enter the distance: "))
NA = float(optical_fiber.Numerical_aperture(D,L))
print("The numerical aperture is: %f"%(NA))


        
