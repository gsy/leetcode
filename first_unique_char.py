# -*- coding: utf-8 -*-


class Solution:
    def firstUniqChar(self, s):
        if len(s) == 0:
            return -1

        buckets = [0] * 26
        for char in s:
            bucket = ord(char) - ord('a')
            buckets[bucket] = buckets[bucket] + 1

        for index, char in enumerate(s):
            bucket = ord(char) - ord('a')
            if buckets[bucket] == 1:
                return index

        return -1
