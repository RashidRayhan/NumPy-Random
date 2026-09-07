from numpy import random
import numpy as np

#Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

#Generate a random permutation of elements of following array:
arry = np.array([1, 2, 3, 4])
print(random.permutation(arry))