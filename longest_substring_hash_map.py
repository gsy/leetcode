# -*- coding: utf-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        longest = 0
        length = 0
        chars = {}
        start_point = None

        for index, char in enumerate(s):
            # 到 index 位置为止，如果都没有重复，那么长度 + 1
            # 如果有重复，重复之后的第一位肯定还没有重复，那个地方算做起点
            # 跟 start_point 之前的重复了，还是计算到 start_point 上就行
            if char not in chars:
                length = length + 1
                chars[char] = index
                if start_point is None:
                    start_point = index
            else:
                if chars[char] + 1 > start_point:
                    start_point = chars[char] + 1
                    length = index - start_point + 1
                    chars[char] = index
                else:
                    length = index - start_point + 1
                    chars[char] = index

            if length > longest:
                longest = length

        return longest
