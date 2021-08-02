###(10)
arr =[]
for i in range(0,100):
    a = input("enter number in an array: ")
    if a != 'stop':
        arr.append(a)
    else:
        break    
print((arr))
s = [float(i) for i in arr]
    
new_list = []

while s:
    minimum = s[0]  # arbitrary number in list 
    for x in s: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    s.remove(minimum)    

print("the list in sorted way is : ",new_list)

l1=[]
for i in new_list:
    if i in l1:
        del i
    else:
        l1.append(i)
print(l1)

#########OR
NumList = []

Num = int(input("Please enter the Total Number of List Elements: "))

for i in range(1, Num + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for i in range (Num):
    for j in range(i + 1, Num):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print("Element After Sorting List in Ascending Order is : ", NumList)


for i in range (Num):
    for j in range(i + 1, Num):
        if(NumList[i] < NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print("Element After Sorting List in Descending Order is : ", NumList)



































