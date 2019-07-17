# -*- coding: utf-8 -*-


class Solution:
    def commonPrefix(self, a, b):
        if a == b:
            return a

        pattern, result = "", ""
        for char in a:
            pattern = pattern + char
            if b.startswith(pattern):
                result = pattern
            else:
                break
        return result

    def longestCommonPrefix(self, strs):
        length = len(strs)
        if length == 0:
            return ""
        elif length == 1:
            return strs[0]

        prev = strs[0]
        for index, string in enumerate(strs):
            if index == 0:
                continue

            prefix = self.commonPrefix(prev, string)
            if prefix == "":
                break
            else:
                prev = prefix

        return prefix


if __name__ == '__main__':
    s = Solution()
    r = s.longestCommonPrefix(["flower", "flow", "flight"])
    assert r == "fl"

    r = s.longestCommonPrefix(["dog", "racecar", "car"])
    assert r == ""
