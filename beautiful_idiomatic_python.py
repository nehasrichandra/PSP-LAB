##Looping backwards:
colors = ['red', 'blue', 'green', 'yellow', 'white', 'black']
#to print the colors backwards
for i in range(len(colors)-1,-1,-1):
    print(colors[i])
#better way
for color in reversed(colors):
    print(color)


##looping over a range of numbers:
for i in [0,1,2,3,4]:
    print(i**2)
#better way:
for i in range(5):
    print(i**2)

    
##nested loop
scores = [90,85,75,87,98,77]
above_90 = 0
below_90 = 0
for i in scores:
    if i>=90:
        above_90 = above_90 + 1
    if not i>=90:
        below_90 = below_90 +1
print(above_90)
print(below_90)
#better way
above_90 = 0
below_90 = 0
for i in scores:
    if i>=90:
        above_90 += 1
    else:
        below_90 += 1
print(above_90)
print(below_90)


##accumlator addition or substraction
temp = [28,25,40,19,15,26,42,41.5]
hot = 0
moderate = 0
cold = 0
for i in temp:
    if float(i)>=40:
        hot = hot + 1
    if 20<float(i)<40:
        moderate = moderate + 1
    if float(i)<20:
        cold = cold + 1
print(hot)
print(moderate)
print(cold)
#better way
hot = 0
moderate = 0
cold = 0
for i in temp:
    if float(i)>=40:
        hot += 1
    if 20<float(i)<40:
        moderate += 1
    if float(i)<20:
        cold += 1
print(hot)
print(moderate)
print(cold)


##printing different contents
print("hot = ",hot)
print("moderate = ",moderate)
print("cold = ",cold)
#better way
print('hot = ',hot,'\n','moderate = ',moderate,'\n','cold = ',cold)


##
print("Hey!")
print("I am Neha")
#better way
print("Hey! \n I am Neha")


##
a=1
b=2
c=3
#better way
a,b,c=1,2,3
print(a,b,c)


##
a = [1,2,3,4,5]
a = a + [5]
print(a)
#better way
nums = [0,1,2,3,4,5]
nums.append('cat')
print(nums)


##
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print (x)
        t = y
        y = x + y
        x = t
print(fibonacci(5))
#better way
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print (x)
        x, y = y, x + y
print(fibonacci(5))

    
##
Colors = ["red","orange","blue","yellow","green","caramine","violet"]

for i in range(len(Colors)):
    print (Colors[i])
#better way
for Color in Colors:
    print(Color)


##     
x=5
y=10
temp=x
x=y
y=temp
print('The value of x after swapping: {}' .format(x))
print('The value ofyx after swapping: {}' .format(y))
#better way
x=5
y=10
x,y=y,x
print("x = ",x)
print("y = ",y)


##removing last item
fruits = ['orange','apple', 'peaches', 'pear', 'watermelon']
#fruits.remove('watermelon')
#print(fruits)
#better way
fruits.pop()
print(fruits)


##updating sequences
fruits = ['orange','apple', 'peaches', 'pear', 'watermelon']
del fruits[0]
fruits.pop(0)
fruits.insert(0,'banana')
print(fruits)
#better way
fruits = ['orange','apple', 'peaches', 'pear', 'watermelon']
del fruits[0]
fruits.popleft()
fruits.appendleft('banana')


##
result = []
for i in range(20):
    s = i**2
    result.append(s)
print(sum(result))
#better way
print(sum(i**2 for i in range(20)))


##
nums = [2,4,6,8,10]
total = 0
for i in nums:
    total = i + total
print(total)
#better way
print(sum(nums))


##
print()
a,b = 1,2
print(a,b)
rev = a
a = b
b = rev
print(a,b)
#better way
print()
a,b =1,2
print(a,b)
a,b=b,a
print(a,b)
