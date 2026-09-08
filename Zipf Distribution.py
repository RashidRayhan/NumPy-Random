from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.zipf(a = 2, size = (2, 3))
print(x)

arr = random.zipf(a = 3, size = 1000)
sns.displot(arr)
plt.show()

arry = random.zipf(a = 5, size = 1000)
sns.displot(arry, kind = "kde")
plt.show()s