import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

x_values = [x for x in range(1,101)]
y_values = [x*x for x in x_values]

plt.scatter(x_values,y_values, c='red', edgecolor='none', s=10)
plt.title("Square Numbers", fontsize=24) #设置标题
plt.xlabel("value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14) #设置刻度样式
plt.axis([0, 110, 0, 11000]) #设置X轴和Y轴的取值范围
plt.show()
