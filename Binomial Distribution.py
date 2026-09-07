from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Binomial Distribution is a Discrete Distribution.
x = random.binomial(n = 10, p = 0.5, size = 10)
print(x)


#Visualization of Binomial Distribution
sns.displot(random.binomial(n=10, p = 0.5, size = 100))
plt.show()

#Difference Between Normal and Binomial Distribution
data ={
    "normal": random.normal(loc = 50, scale = 5, size = 1000),
    "binomial": random.binomial(n= 100, p = 0.5, size = 1000)
}
sns.displot(data, kind= "kde")
plt.show()