# -*- coding: utf-8 -*-


class Solution:
    def brokenCalc(self, x, y):
        if (x >= y):
            return x - y
        elif (y / x == 2):
            return 1

        if y % 2 == 0:
            # 有两种办法可以到这个地方，但是总是走底下这条？
            # 什么时候走 y+1 那条路？
            # (y+2)/2  = y/2 + 1
            # 加法需要走3次，除法只用走2次，所以可以贪心地走除法
            return 1 + self.brokenCalc(x, int(y / 2))
        else:
            return 1 + self.brokenCalc(x, y + 1)
