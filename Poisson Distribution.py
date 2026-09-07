from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Poisson Distribution is a Discrete Distribution.
x = random.poisson(lam = 10, size= 10)
print(x)

#Visualization of Poisson Distribution
sns.displot(random.poisson(lam = 2, size = 10))
plt.show()

#Difference Between Normal, binomial and Poisson Distribution
dataset = {
    "normal": random.normal(loc = 10, scale = 5, size = 1000),
    "binomial": random.binomial(n = 10, p = 0.5, size = 1000),
    "poisson": random.poisson(lam = 10, size = 1000)
}
sns.displot(dataset, kind = "kde")
plt.show()