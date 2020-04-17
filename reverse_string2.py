# -*- coding: utf-8 -*-


class Solution:
    def reverseStr(self, s, k):
        start, step = 0, k
        result = ""
        while start < len(s):
            middle, end = start + step, start + 2 * step
            left, right = s[start:middle], s[middle:end]
            result = result + left[::-1] + right
            start = start + 2 * step
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.reverseStr("abcdefg", k=2)
    assert r == "bacdfeg"

    r = s.reverseStr("", k=2)
    assert r == ""

    r = s.reverseStr("a", k=2)
    assert r == "a"

    r = s.reverseStr("ab", k=2)
    assert r == "ba"

    r = s.reverseStr("abc", k=2)
    assert r == "bac"

    r = s.reverseStr("abcd", k=2)
    assert r == "bacd"
