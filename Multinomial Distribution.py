from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.multinomial(n = 6, pvals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
sns.displot(x, kind = "kde")
plt.show()
