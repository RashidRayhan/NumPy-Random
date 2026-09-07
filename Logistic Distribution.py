from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Logistic Distribution
y = random.logistic(loc = 10, scale = 20, size = 10)
print(y)

#Visualization of Logistic Distribution
sns.displot(random.logistic(loc = 10, scale = 30, size = 100))
plt.show()

##Difference Between Normal, binomial, Poisson, logistic and uniform Distribution
dataset ={
    "normal": random.normal(loc= 10, scale = 10, size = 100),
    "binomial": random.binomial(n= 10, p = 0.5, size = 100),
    "poisson": random.poisson(lam = 10, size = 100),
    "uniform": random.uniform(low = 10, high = 10, size= 100),
    "logistic": random.logistic(loc = 10, scale = 10, size = 100)
}
sns.displot(dataset, kind = "kde")
plt.show()