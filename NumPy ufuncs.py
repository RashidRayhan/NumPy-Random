import numpy as np

#Without ufunc, we can use Python's built-in zip() method:
x = [1, 2, 4, 6]
y = [4, 6, 9, 5]
z = []
for j , i in zip(x, y):
    z.append (j + i)
print(z)

#With ufunc, we can use the add() function:
a = [1, 2, 4, 6]
b = [4, 6, 9, 5]
c = np.add(a, b)
print(c)

#Create Your Own ufunc
def myadd(x, y):
    return x + y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [3, 4, 6, 7]))

#Check the data type
print(type(myadd))
#check concatenate type
print(type(np.concatenate))

#Use an if statement to check if the function is a ufunc or not:
if type(np.add) == np.ufunc:
    print("Add is unfunc")
else:
    print ("Add is not unfunc")

#Simple Arithmetic
#use for add() aditiona
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr = np.add(arr1, arr2)
print(arr)

#Use subtraction
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arry = np.subtract(arr1, arr2)
print(arry)

#Use multiplication
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.multiply(arr1, arr2)
print(arr3)

#Use Division
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arry1 = np.divide(arr1, arr2)
print(arry1)

#user power
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr1 = np.power(arr1, arr2)
print(arr1)

#user mod/remainder/divmod/absolute all are same result
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr2 = np.mod(arr1, arr2)
print(arr2)