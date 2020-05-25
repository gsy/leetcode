#!/usr/bin/env python3

class Solution:
    def buildArray(self, target, n):
        result = []
        ls = [i for i in range(1, n+1)]
        length = len(target)

        for num in target:
            while True:
                x = ls.pop(0)
                if x == num:
                    result.append("Push")
                    break
                else:
                    result.append("Push")
                    result.append("Pop")

        return result
