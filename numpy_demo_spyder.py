# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 09:43:46 2021

@author: neha
"""

import numpy as np

#example
data = np.random.randn(3,4)
print(data)
print("\n")
data = data*10
print(data)
data = data + data
print("\n")
print(data)


#Creating ndarrays
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.shape) #for no. of rows and columns
print(type(arr))

#to find the element in the array
print(arr[0,0])
print(arr[0,1])
print(arr[1,0])
#to print all the elements in row
print(arr[1,:])
#to print all the elements in column
print(arr[:,0])


#Aritmetic with NumPy Arrays
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
arr = arr * arr
print(arr)
arr = arr - arr
print(arr)
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr = 1/arr
print(arr)
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr = arr*0.5
print(arr)


##Basic Indexing and Slicing
arr = np.arange(10)
print(arr)

print(arr[4])
print(arr[5:8])

arr[5:8] = 12
arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
print(arr_slice)
print(arr)
#'bare' slice [:]
arr_slice[:] = 64
print(arr)
#To copy a slice of array:
#    arr[5:8].copy()
# Two dimensional arrays
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d[2])
#to select individual element
print(arr2d[0][2])
#or
print(arr2d[0,2])
#three dimensional matrix
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d.shape)
#arr3d[0] is a 2 x 3 array
old_values = arr3d[0].copy()
print(old_values)
print(arr3d[0])
arr3d[0] = 42
print(arr3d)
arr3d[0] = old_values
print(arr3d)
print(arr3d[1,0])
x = arr3d[1]
print(x)
print(x[0])

#Indexing with slices
print(arr)
print(arr[1:6])
print(arr2d[:2])
print(arr2d[:2,1:])
print(arr2d[1,:2])
print(arr2d[:2,2])
print(arr2d[:,:1])
arr2d[:2,1:] = 0
print(arr2d)


##Boolean indexing
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data = np.random.randn(7,4)
print(names)
print(names.dtype)
print(data)
print(names == 'Bob')
print(data[names == 'Bob'])
print(data[names == 'Bob',2:])
print(data[names == 'Bob',3])
print(names != 'Bob')
print(names.dtype)


#Fancy indexing
arr = np.empty((8,4))
for i in range(8):
    arr[i]=i
print(arr)
print(arr[[4,3,0,6]])
print(arr[[-3,-5,-7]])
arr = np.range(32).reshape((8,4))
print(arr)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])


##Transposing Arrays and swaping Axes
arr = np.arange(15).reshape((3,5))
print(arr)
print(arr.T) #Here T is transpose of the matrix
arr = np.random.randn(6,3)
print(arr)
print(np.dot(arr.T,arr))
arr = np.arange(16).reshape((2,2,4))
print(arr)
print(arr.transpose((1,0,2)))
print(arr)
print(arr.swapaxes(1,2))


##Universal Functions: Fast Element-Wise Array Functions
arr = np.arange(10)
print(arr)
print(np.sqrt(arr))
print(np.exp(arr))
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)
print(np.maximum(x,y))
print(np.minimum(x,y))
arr = np.random.randn(7)*5
print(arr)
remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)
print(arr)
print(np.sqrt(arr))
print(np.sqrt(arr,arr))


##Array-Oriented Programming with Arrays
points = np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
print(ys)
z = np.sqrt(xs**2+ys**2)
print(z)


## Expressing Conditional Logic as Array Operations
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y)
          for x, y, c in zip(xarr, yarr, cond)]
print(result)


#Mathematical and statistical methods
arr = np.random.randn(5,4)
print(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())
print(arr.mean(axis=1))
print(arr.sum(axis=0))
arr = np.array([0,1,2,3,4,5,6,7])
print(arr.cumsum())
arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(arr)
print(arr.cumsum(axis=0))
print(arr.cumprod(axis=1))


##Methods of Boolean Arrays
arr = np.random.randn(100)
print((arr>0).sum())
bools = np.array([False,False,True,False])
print(bools.any())
print(bools.all())


##Sorting
arr = np.random.randn(6)
print(arr)
print(arr.sort)
arr = np.random.randn(4,4)
print(arr)
print(arr.sort(1))


##Unique and other set logic
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))
print(names.dtype)
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
print(sorted(set(names)))
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))


## File Input and Output with Arrays
arr = np.arange(10)
np.save('some_array', arr)
print(np.load('some_array.npy'))
np.savez('array_archive.npz', a=arr, b=arr)
arch = np.load('array_archive.npz')
print(arch['b'])


##Linear algebra
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x)
print(y)
print(x.dot(y))
print(np.dot(x,y))
print( np.dot(x, np.ones(3)))
print( x @ np.ones(3))


## Examples of random walks
import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)


##Simulating many random walks at once
nwalks = 5000
nsteps = 1000
draws = np.random.randit(0,2,size=(nwalks,nsteps))
steps = np.where(draws>0,1,-1)
walks = steps.cumsum(1)
print(walks)
print(walks.max())
print(walks.min())
hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print(hits30.sum())
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print( crossing_times.mean())

    








