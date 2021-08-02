'''##(1)We can define the sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1: 1, if x = 1 x + sum from 1 to x-1 if x > 1 Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 recursively: 
def Sum(n):
    if n <= 1:
        return n
    else:
        return n + Sum(n - 1)
          
n = int(input("Enter the value of n= "))
print(Sum(n))'''




'''##(2) Given an integer 'n' write a program to generate a dictionary with (i, i*i) such that i is  an integer between 1 and n (both included). The program should then print the dictionary. 
n=int(input("Enter the value of n: "))
dict = {}
squares= {i: i*i for i in range(1, n+1)}
print(squares)
for i in range(1,n+1):
    dict[i] = i*i
    
print(dict)'''

    


'''##(3a) Write a program to print each line of a file in reverse order.
f = open("text.txt",'r')
data = f.read()
data_split = data.split("\n")
print(data_split)
r = data_split[::-1]
print(r)

#(3b) Write a program to compute the number of characters, words and lines in a file.
f=open("text.txt","r")
data = f.read()
total_charac = len(data)
print("Total charcaters = ",total_charac)
data_split = data.split()
number_of_words = len(data_split)
print("number of words = ",number_of_words)
number_of_lines = data.split("\n")
n = len(number_of_lines)
print("number of lines = ",n)'''


'''##(4a) Write a function dups to find all duplicates in the list. 
a=[1,2,3,3,4,5,6,7,4,3,9,1,2,2]
import collections
print([item for item, count in collections.Counter(a).items() if count>1])
l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')

#(4b) Write a function unique to find all the unique elements of a list.
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = list(set(numbers))    #here we use a set to get the unique numbers then turn the set into a list
print(unique_numbers)

l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i in l1:
        print(i,end=' ')
    else:
        l1.append(i)'''
        



'''##(5a)  Write a function cumulative_product to compute cumulative product of a list of numbers.
from math import prod
def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [prod(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]
 
    
input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
# print list
print('list: ', user_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i]) 
# Driver Code
#lists = [10, 20, 30, 40, 50]
print (Cumulative(user_list))

#(5b) Write a function reverse to reverse a list. Without using the reverse function.            
def Reverse(numbers):
      # Base case when the list is only one item
      if (len(numbers)==1):
         return numbers
      # Otherwise
      return Reverse(numbers[1:]) + numbers[0:1]
 

print(Reverse(user_list)) '''


'''##(6a) Write a program that defines a matrix and prints.
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
  
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()'''

'''#(6b) Write a program to perform addition of two square matrices.
X = [[2,2,3],
    [4 ,3,6],
    [7 ,8,4]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)'''


'''#(6c) Write a program to perform multiplication of two square matrices
# 4x4 matrix multiplication using Python3
# Function definition
def matrix_multiplication(M, N):
	# List to store matrix multiplication result
	R = [[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]]

	for i in range(0, 4):
		for j in range(0, 4):
			for k in range(0, 4):
				R[i][j] += M[i][k] * N[k][j]

	for i in range(0, 4):
		for j in range(0, 4):
			# if we use print(), by default cursor moves to next line each time,
			# Now we can explicitly define ending character or sequence passing
			# second parameter as end ="<character or string>"
			# syntax: print(<variable or value to print>, end ="<ending with>")
			# Here space (" ") is used to print a gape after printing
			# each element of R
			print(R[i][j], end =" ")
		print("\n", end ="")

# First matrix. M is a list
M = [[1, 1, 1, 1],
	[2, 2, 2, 2],
	[3, 3, 3, 3],
	[4, 4, 4, 4]]

# Second matrix. N is a list
N = [[1, 1, 1, 1],
	[2, 2, 2, 2],
	[3, 3, 3, 3],
	[4, 4, 4, 4]]
	
# Call matrix_multiplication function
matrix_multiplication(M, N)'''


'''from fractions import Fraction
   
print (Fraction(10, 2) * Fraction(20, 3))

#7
# Python3 program to add 2 fractions

# Function to return gcd of a and b
def gcd(a, b):
	if (a == 0):
		return b;
	return gcd(b % a, a);

# Function to convert the obtained
# fraction into it's simplest form
def lowest(den3, num3):

	# Finding gcd of both terms
	common_factor = gcd(num3, den3);

	# Converting both terms
	# into simpler terms by
	# dividing them by common factor
	den3 = int(den3 / common_factor);
	num3 = int(num3 / common_factor);
	print(num3, "/", den3);

# Function to add two fractions
def addFraction(num1, den1, num2, den2):

	# Finding gcd of den1 and den2
	den3 = gcd(den1, den2);

	# Denominator of final
	# fraction obtained finding
	# LCM of den1 and den2
	# LCM * GCD = a * b
	den3 = (den1 * den2) / den3;

	# Changing the fractions to
	# have same denominator Numerator
	# of the final fraction obtained
	num3 = ((num1) * (den3 / den1) +
			(num2) * (den3 / den2));

	# Calling function to convert
	# final fraction into it's
	# simplest form
	lowest(den3, num3);

# Driver Code
num1 = 1; den1 = 500;
num2 = 2; den2 = 1500;

print(num1, "/", den1, " + ", num2, "/",
	den2, " is equal to ", end = "");
addFraction(num1, den1, num2, den2);'''


'''7.Any fraction can be written as the division of two integers. 
You could express this in  Python as a tuple – (numerator, denominator). 
Write functions for each of the following. 
They must use the tuple representation to return fractions. 
        a. Given two fractions as tuples, multiply them. 
        b. Given two fractions as tuples, divide them. 
        c. Given a list of fractions as a tuple, return the one 
           that is smallest in value. Also write a small command-line 
            interface such that the user running your script 
            
            
input_string = input('Enter numerator and denominator of a list separated by space ')
print("\n")
user_list_1 = input_string.split()
# print list
print('list: ', user_list_1)

# convert each item to int type
for i in range(len(user_list_1)):
    # convert each item to int type
    user_list_1[i] = int(user_list_1[i])
    
    
x = tuple(user_list_1)    
print(x)

num_1 = x[0]
print(num_1)
den_1 = x[1]
print(den_1)

input_string = input('Enter numerator and denominator of a list separated by space ')
print("\n")
user_list_2 = input_string.split()
# print list
print('list: ', user_list_2)

# convert each item to int type
for i in range(len(user_list_2)):
    # convert each item to int type
    user_list_2[i] = int(user_list_2[i])
    
    
y = tuple(user_list_2)    
print(y)
num_2 = y[0]
print(num_2)
den_2 = y[1]
print(den_2)

#(a)
final_num_1 = (num_1)*(num_2)
final_den_1 = (den_1)*(den_2)
print(final_num_1)
print(final_den_1)

final_frac_1 = (final_num_1,final_den_1)
print(final_frac_1)

#(b)
final_num_2 = (num_1)*(den_2)
final_den_2 = (den_1)*(num_2)
print(final_num_2)
print(final_den_2)

final_frac_2 = (final_num_2,final_den_2)
print(final_frac_2)

#(c)
input_string = input('Enter numerator and denominator of a list separated by space ')
print("\n")
user_list_3 = input_string.split()
# print list
print('list: ', user_list_3)

# convert each item to int type
for i in range(len(user_list_3)):
    # convert each item to int type
    user_list_3[i] = int(user_list_3[i])
    
print(user_list_3) 

OR
# Function to return gcd of a and b
def gcd(a, b):
	if (a == 0):
		return b;
	return gcd(b % a, a);

# Function to convert the obtained
# fraction into it's simplest form
def lowest(den3, num3):

	# Finding gcd of both terms
	common_factor = gcd(num3, den3);

	# Converting both terms
	# into simpler terms by
	# dividing them by common factor
	den3 = int(den3 / common_factor);
	num3 = int(num3 / common_factor);
	print(num3, "/", den3);

# Function to add two fractions
def addFraction(num1, den1, num2, den2):

	# Finding gcd of den1 and den2
	den3 = gcd(den1, den2);

	# Denominator of final
	# fraction obtained finding
	# LCM of den1 and den2
	# LCM * GCD = a * b
	den3 = (den1 * den2) / den3;

	# Changing the fractions to
	# have same denominator Numerator
	# of the final fraction obtained
	num3 = ((num1) * (den3 / den1) +
			(num2) * (den3 / den2));

	# Calling function to convert
	# final fraction into it's
	# simplest form
	lowest(den3, num3);

# Driver Code
num1 = 1; den1 = 500;
num2 = 2; den2 = 1500;

print(num1, "/", den1, " + ", num2, "/",
	den2, " is equal to ", end = "");
addFraction(num1, den1, num2, den2);'''





'''##(9)
arr =[]
for i in range(0,100):
    a = input("enter numbers in an array: ")
    if a != 'stop':
        arr.append(a)
    else:
        break    
print((arr))
even = []
odd = []
s = [int(i) for i in arr]
for j in s:
    if (j % 2) == 0:  
        even.append(j)
    else:
        odd.append(j)
        
print(even)
print(odd)



add = sum(s)
print(add)
n = len(s)
average = add/n
print(average)

add_even = sum(even)
print(add_even)
n_even = len(even)
average_even = add_even/n_even
print(average_even)

add_odd = sum(odd)
print(add_odd)
n_odd = len(odd)
average_odd = add_odd/n_odd
print(average_odd)'''








'''###(10)
arr =[]
for i in range(0,100):
    a = input("enter number in an array: ")
    if a != 'stop':
        arr.append(a)
    else:
        break    
print((arr))
s = [int(i) for i in arr]
    
new_list = []

while s:
    minimum = s[0]  # arbitrary number in list 
    for x in s: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    s.remove(minimum)    

print(new_list)

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

print("Element After Sorting List in Descending Order is : ", NumList)'''












'''##(11) Write the following functions: overlap() Given two lists, find a list of the elements common to both lists and return it. join() Given two lists, join them together to be one list without duplicate elements and return that list.
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")
          

n = int(input("Enter number of numbers in first list : "))
m = int(input("Enter number of numbers in second list : "))
list1 = []
for i in range(0,n):
    a = input(int())
    list1.append(a)
print(list1)
list2 = []
for i in range(0,m):
    b = input(int())
    list2.append(b)
print(list2)

t = list1 + list2
a  = list(set(t))
print(sorted(a))'''











'''##(12) Create a tuple of student’s data by including roll no, name, and marks for 3 subjects. What will be the output of t = tuple(‘TutorialAICSIP’)?  Explain it.
tup = (49,'neha',10)
subject = ('maths','english','psp')
t = tuple('TutorialAICSIP')
print(t)
##OR
class student :
    mark = [ ]
    def getData(self,rn,name,m1,m2,m3):
        student.rn = rn
        student.name = name
        student.mark.append(m1)
        student.mark.append(m2)
        student.mark.append(m3)


    def displayData(self):
        print(" Roll no is :- ",student.rn)
        print(" Name :- ",student.name)
        print(" Marks :- ",student.mark)

    def total(self):

        return(student.mark[0] + student.mark[1] + student.mark[2])

r = int(input("Enter the roll no :-"))
name = input(" Enter the name :- ")
m1 = int(input(" Enter the mark in first subject :- "))
m2 = int(input(" Enter the mark in second subject :- "))
m3 = int(input(" Enter the mark in third subject :- "))

s1 = student()
s1.getData(r,name,m1,m2,m3)
s1.displayData()
print(" total mark :- ",s1.total())
t = tuple('TutorialAICSIP')
print(t)'''













'''##(13)  a) Write a program to read email IDs of n number of students and store them in a tuple. Create two new tuples, one to store only the usernames from the email IDs and second to store domain names from the email ids. Print all three tuples at the end of the program. 
    #  b) Write a program to input names of n students and store them in a tuple. Also, input a name from the user and find if this student is present in the tuple or not. We can accomplish these by: (a) writing a user defined function (b) using the built-in function.
n = int(input("Enter number of students : "))
list1=[]
for i in range(n):
    email=input("Enter email: ")
    list1.append(email)
tuple1=tuple(list1)
names=[]
domains=[]
for i in tuple1:
    name,domain = i.split("@") #return list of strings break using the string in the argument
    names.append(name) #build names list
    domains.append(domain) #build domains list
names = tuple(names)
domains = tuple(domains)
print("Tuple = ",tuple1)
print("Names = ",names)
print("Domains = ",domains)'''


'''
#13b) Write a program to input names of n students and store them in a tuple. Also, input a name from the user and find if this student is present in the tuple or not. We can accomplish
#these by: (a) writing a user defined function (b) using the built-in function.
n = int(input("Enter the number of students: "))
list1 = []
for i in range(n):
    name = input() 
    list1.append(name)
# makes a tuple from the list of names
tuple1 = tuple(list1)
findName = input("Enter name to find: ")
#   part (a) a user defined function to search
def userDefinedSearch():
     #loops through every element of tuple
    for item in tuple1:
         #if any element is equal to what we are finding
        if item==findName:
            #announce item found
            print("Name found") 
            return #return from the function
    #this statement is reached only if the element is not found
    print("Name not found")

#calling user defined function
userDefinedSearch()

# part (b) built in function
# index() returns the first index where element is found
# the return value will be either 0 or more than 0 if the element is present in the tuple 
if tuple1.index(findName) >=0 :
    print("Name found")
else:
    print("Name not found")'''








'''##(14)
n = int(input("Enter how many names you want to enter: "))
# initialize empty dictionary
names={}
for i in range(n):
    name=input("Enter name of friend: ")
    number=input("Enter phone number: ")
    names[name]=number #add name number to dictionary
print(names)
names["Arun"]="9877666234" #add new item
print("Modified dictionary ",names)
del names["Arun"] #delete an item
print(names)
for name in names: #modify first key value
    names[name] = "9456356344"
    break
print("Amit" in names)
print("dictionary in sorted order")
for i in sorted (names) : #sort the dictionary
    print((i, names[i]), end =" ")'''








    
    
'''##(15)
#(15a)
f=open("text.txt","r")
data = f.read()
print(data)
#(15b)
total_charac = len(data)
print("Total charcaters = ",total_charac)
data_split = data.split()
number_of_words = len(data_split)
print("number of words = ",number_of_words)
#(15c)
accum =0 
for i in data_split:
    if i == 'is':
        accum += 1
print(accum)        
#(15d)
e = 0
for i in data_split:
    if i[-1] == 'e':
        e += 1
print(e)'''













    
    
        
    



















