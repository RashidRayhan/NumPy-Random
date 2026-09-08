from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.exponential(scale = 10, size = (2, 3))
print(x)


arr = random.exponential (scale = 10, size = (2, 3))
sns.displot(arr, kind = "kde")
plt.show()