import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')


data = pd.read_csv('Scatter.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']


plt.scatter(view_count,likes, c=ratio, cmap='summer',
            edgecolor='black', linewidth=1, alpha = 0.75)

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.xscale('log')
plt.yscale('log')

cbar =   plt.colorbar()
cbar.set_label("Ratio")


plt.tight_layout()

plt.show()
