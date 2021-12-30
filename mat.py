from matplotlib import pyplot as plt

plt.style.use('seaborn')

fig1,ax1= plt.subplots()
fig2,ax2= plt.subplots()
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [1000, 2242, 11246, 22249, 22253,56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [33345, 33348, 33353, 33357, 33363,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [44437, 44443, 44446, 44449,44453,
            56373, 62375, 66674, 68745, 68746, 74583]

ax1.plot(dev_x, dev_y)
ax2.plot(dev_x,js_dev_y,linewidth=2)
ax2.plot(dev_x,py_dev_y)

ax1.legend(['All Devs','Python','JavaScript'])
ax1.set_title("Salary by age")
ax1.set_ylabel("Salaries")


ax2.legend(['All Devs','Python','JavaScript'])
ax2.set_xlabel("Ages")
ax2.set_ylabel("Salaries")


plt.tight_layout()

fig1.savefig('fig1.png')
fig2.savefig('fig2.png')
plt.show()
