from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr = random.chisquare(df = 2, size = (2, 3))
print(arr)

arry = random.chisquare(df = 10, size = 100)
sns.displot(arry, kind = "kde")
plt.show()