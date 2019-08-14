# -*- coding: utf-8 -*-

class Solution:
    def combinationSum(self, candidates, target):
        combination = {}
        # 这里面没有重复的元素
        # [2, 3, 6, 7]
        # 怎么组合？比如说我一定要用2,能拿到[2, 4, 6, 8],这个集合给其他数字组合
        # [2, 4, 6, 8], [3, 6], [6], [7]
        for candidate in candidates:
            current = candidate
            while current <= target:
                ls = combination.get(candidate, [])
                ls.append(current)
                combination[candidate] = current
                current = current + candidate
