#dictionaries demo

''' A dictionary in python is the unordered and changeable collection of
data values that holds key-value pairs.'''

'''A dictionary in python is declared by enclosing a comma-seperated
list of key-value pairs using curly braces({}).'''

'''Syntax for python Dictionary'''
# key:value

#example--
'''student1 = {'Name':'Neha','branch':'ECE','section':'A1','Roll_no':49}
print(type(student1))
print(student1)'''

#the key 'name' is overlapping and printing the last value
'''student1 = {'Name':'Neha','branch':'ECE','section':'A1','Roll_no':49,'Name':'chandra'}
print(student1)
print(student1['branch'])'''

#adding another key n value we should use 'update' and put in curly
#brackets ({})
'''student1 = {'Name':'Neha','branch':'ECE','section':'A1','Roll_no':49}
student1.update({'Member':'NCC'})
print(student1)'''

# to delete
'''student1 = {'Name':'Neha','branch':'ECE','section':'A1','Roll_no':49}
print("before deleting")
print(student1)
del student1['Name']
print("After deleting")
print(student1)'''

# list of tuples in dictionary
'''print(student1.items())'''

#to check a particular 'key' is ther or not
'''student1 = {'Name':'Neha','branch':'ECE','section':'A1','Roll_no':49}
print("Keys of student1 are")
print(student1.keys())

for i in student1.keys():
    print(student1[i])'''

# for 'values'
student1 = {'Name':'Neha','branch':'ECE','section':'A1','Roll_no':49}
print(student1.values())


