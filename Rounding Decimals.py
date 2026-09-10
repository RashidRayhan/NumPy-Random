from math import log
import numpy as np

#Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
arr = np.trunc([-3.1666, 3.6667])
print(arr)

#fix are same as wrok
arry = np.fix([-3.1666, 3.6667])
print(arry)

#The around() function increments preceding digit or decimal by 1 if >=5 else do nothing. E.g. round off to 1 decimal point, 3.16666 is 3.2
arr1 = np.around([3.1666, 2])
print(arr1)

#The floor() function rounds off decimal to nearest lower integer. E.g. floor of 3.166 is 3.
arr2 = np.floor([-3.1666, 3.6667])
print(arr2)

#The ceil() function rounds off decimal to nearest upper integer. E.g. ceil of 3.166 is 4.

arr3 = np.ceil([-3.1666, 3.6667])
print(arr3)


#NumPy Logs
#Use the log2() function to perform log at the base 2.

arr = np.arange(1, 5)
print(np.log2(arr))

#Use the log10() function to perform log at the base 10.
arr4 = np.arange(1, 10)
print(np.log10(arr4))

#Use the log() function to perform log at the base e.
arr5 = np.arange(1, 10)
print(np.log(arr5))

#NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter:
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))

#NumPy Summations use add and output result will be [2, 4, 6]
ar1 = np.array([1, 2, 3])
ar2 = np.array([1, 2, 3])
arr3 = np.add(ar1, ar2)
print(arr3)

#Now add sum and see output result is 12
ar4 = np.array([1, 2, 3])
ar5 = np.array([1, 2, 3])
ar6 = np.sum([ar4, ar5])
print(ar6)

#Single sum work result see result is [6 6]
ar7 = np.array([1, 2, 3])
ar8 = np.array([1, 2, 3])
ar9 = np.sum([ar7, ar8], axis = 1)
print(ar9)


#Cummulative Sum

arr6 = np.array([1, 2, 3, 4])
arr7 = np.cumsum(arr6)
print(arr7)

#NumPy Products
ar10 = np.array([1, 2, 3, 4])
ar11 = np.prod(ar10)
print(ar11)

#Find the product of the elements of two arrays:
ar12 = np.array([1, 2, 3, 4])
ar13 = np.array([1, 2, 3, 4])
print(np.prod([ar12, ar13]))

#If you specify axis=1, NumPy will return the product of each array.
ar14 = np.array([1, 2, 3, 4])
ar15 = np.array([1, 2, 3, 4])
print(np.prod([ar14, ar15], axis = 1))

#Perfom partial sum with the cumprod() function.
arr16 = np.array([1, 2, 3, 4])
print(np.cumprod(arr16))