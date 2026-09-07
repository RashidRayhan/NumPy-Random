from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.uniform(low = 10, high = 20, size = 10)
print(x)

#Visualization of Uniform Distribution
sns.displot(random.uniform(low = 5, high = 10, size = 100))
plt.show()

##Difference Between Normal, binomial, Poisson and uniform Distribution
dataset = {
    "normal": random.normal(loc = 10, scale = 5, size = 1000),
    "binomial": random.binomial(n = 10, p = 0.5, size = 1000),
    "poisson": random.poisson(lam = 10, size = 1000),
    "uniform": random.uniform(low = 10, high = 20, size = 1000)
}
sns.displot(dataset, kind = "kde")
plt.show()