#Matplotlib制图
#折线图
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X轴标签')
plt.ylabel('Y轴标签')
plt.title('折线图')
plt.show()

#散点图
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y)
plt.xlabel('X轴标签')
plt.ylabel('Y轴标签')
plt.title('散点图')
plt.show()

#柱状图
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 1, 5, 9]

plt.bar(categories, values)
plt.xlabel('类别')
plt.ylabel('值')
plt.title('柱状图')
plt.show()
