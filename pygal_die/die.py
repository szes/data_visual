# -*- coing=utf-8 -*-

from random import randint

class Die(object):
    """骰子类"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """随机返回骰子一面数"""
        return randint(1, self.num_sides)
