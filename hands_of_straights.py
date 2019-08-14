# -*- coding: utf-8 -*-

class Solution:
    def count(self, hand):
        result = {}
        for num in hand:
            result[num] = result.get(num, 0) + 1
        return result

    def isNStraightHand(self, hand, size):
        length = len(hand)
        if length < size or length % size != 0:
            return False

        groups = length / size
        nums = self.count(hand)
        # 按照 key 从小到大排列
        items = sorted(nums.items(), key=lambda item: item[0])
        for num, value in items:
            # 同一个数，分配到不同的集合里面
            if value > groups:
                return False

            #



        # 1, 2, 2, 3, 3, 4, 6, 7, 8
        # 按照 key 分组，如果是连续的，那么可以排成连续的
        # key 分完了，得看 value 是不是匹配的, groups = length / size
        # keys = [1, 2, 3, 4, 6, 7, 8], 分成3组 1, 2, 3|2, 3, 4|6, 7, 8
