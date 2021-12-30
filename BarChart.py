from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

plt.style.use("fivethirtyeight")

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes = np.arange(len(ages_x))
width = 0.25

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes-width,py_dev_y,label = 'Python', width = width)

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_indexes,dev_y,label = 'All Devs',width = width)

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes+width,js_dev_y,label = 'Script',width = width)

plt.title("Median Salary by Age")
plt.legend()
plt.tight_layout()
plt.xticks(ticks=x_indexes, labels=ages_x)


plt.show()
