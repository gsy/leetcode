# -*- coding: utf-8 -*-


class Solution:
    def compress(self, chars):
        result, count = "", 0
        for char in chars:
            if prev and char == prev:
                count = count + 1
            else:
                prev = char
                count = 1




if __name__ == '__main__':
    s = Solution()
    r = s.compress(["a","a","b","b","c","c","c"])
    print(r)
