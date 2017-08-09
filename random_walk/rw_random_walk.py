# add by gaozhi

from matplotlib import pyplot as plt
from random_walk import RandomWalk

def rw_random_walk1(nums):
    """显示随机漫步数据-数据点"""
    rw = RandomWalk(nums)
    rw.fill_walk()
    point_numbers = list(range(rw.num_point))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    plt.scatter(0, 0, c='green', edgecolor='none', s=50)   # 起点为绿色
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=50) # 终点为红色

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()


def rw_random_walk2(nums):
    """显示随机漫步数据-折线"""
    rw = RandomWalk(nums)
    rw.fill_walk()
    point_numbers = list(range(rw.num_point))

    plt.plot(rw.x_values, rw.y_values)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

if __name__ == "__main__":
    print("start random walk")

    while True:

        rw_random_walk1(5000)

        keep_run = input("Make anthoer Walk? (y/n):")
        if keep_run == 'n':
            break
