# -*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.cache = {}

    def power(self, x, i):
        key = "{}-{}".format(x, i)
        if key in self.cache:
            return self.cache[key]

        if i == 0:
            result = 1
        else:
            result = 1
            for tmp in range(i):
                result = result * x
        self.cache[key] = result
        return result

    def powerfulIntegers(self, x, y, bound):
        i, j = 0, 0
        x, y = min(x, y), max(x, y)
        result = set()

        if x == 1 and y == 1:
            if 2 <= bound:
                return [2]
            else:
                return []
        elif x == 1:
            while True:
                power_x = 1
                power_y = self.power(y, j)
                integer = power_x + power_y
                if integer <= bound:
                    result.add(integer)
                    j = j + 1
                else:
                    break
        else:
            while True:
                power_x = self.power(x, i)
                power_y = self.power(y, j)
                integer = power_x + power_y
                if integer <= bound:
                    result.add(integer)
                    i = i + 1
                else:
                    if power_y < bound:
                        i = 0
                        j = j + 1
                    else:
                        break

        return list(result)
