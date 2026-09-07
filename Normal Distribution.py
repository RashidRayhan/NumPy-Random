from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


#Generate a random normal distribution of size 2x3:
x = random.normal(size =(2, 3))
print(x)

#Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
y = random.normal(loc = 1, scale = 2, size = (2, 3))
print(y)

#Visualization of Normal Distribution
sns.displot(random.normal(size = 1000), kind = "kde")
plt.show()

