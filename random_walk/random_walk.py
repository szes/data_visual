# -*- coding=utf-8 -*-

# add by gaozhi

import random


class RandomWalk(object):
    """一个生成随机漫步数据的类"""

    def __init__(self, num_point=5000):
        """初始化随机漫步的属性"""
        self.num_point = num_point

        # 所以随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = random.choice([1,-1])
        distance = random.choice([1,2,3,4])
        return direction * distance

    def fill_walk(self):
        """计算随机漫步包含的所有坐标点"""

        # 不断漫步,直到生成所有的坐标点
        while len(self.x_values) < self.num_point:

            # 计算X轴下一个坐标点的方向及距离
            # x_direction = random.choice([1,-1])
            # x_distance = random.choice([1,2,3,4])
            # x_step = x_direction * x_distance
            x_step = self.get_step()

            # 计算X轴下一个坐标点的方向及距离
            # y_direction = random.choice([1,-1])
            # y_distance = random.choice([1,2,3,4])
            # y_step = y_direction * y_distance
            y_step = self.get_step()

            if x_step ==0 and y_step == 0:
                continue

            # 计算下一个点的X值和Y值
            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)
