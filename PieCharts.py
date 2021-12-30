from matplotlib import pyplot as plt

plt.style.use('seaborn-dark')

slices = [3880, 4808, 4994, 5336, 12069]
labels = ['Assembly', 'Go', 'Ruby', 'Other(s):', 'C']
explode = [0,0,0,0.1,0]

plt.pie(slices, labels=labels,wedgeprops={'edgecolor':'black'},
        shadow=True,startangle=30, explode=explode,
        autopct='%1.1f%%')


plt.title("My owesome Pie Chart")
plt.tight_layout()
plt.show()
