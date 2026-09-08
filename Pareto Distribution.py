from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.pareto(a = 3, size = (2, 3))
print(x)

arr = random.pareto(a = 1, size = 100)
sns.displot(arr, kind = "kde")
plt.show()

arry = random.pareto(a = 3, size = 100)
sns.displot(arr)
plt.show()