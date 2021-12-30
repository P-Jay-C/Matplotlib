import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn-notebook')

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [10, 20, 30, 40, 50, 60]

plt.hist(ages, bins = bins,  edgecolor='black')


plt.title(label="Ages")
plt.show()
