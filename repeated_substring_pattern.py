# -*- coding: utf-8 -*-
# https://leetcode-cn.com/problems/repeated-substring-pattern/


class Solution:
    def is_repeated(self, s, length, step):
        if step >= length:
            return False

        start, pattern = 0, None
        while start < length:
            current = s[start: start + step]
            if pattern is None:
                pattern = current
            elif pattern != current:
                return False
            start = start + step
        return True

    def repeatedSubstringPattern(self, s):
        length = len(s)
        if length <= 1:
            return False

        for step in range(int(length/2), 0, -1):
            if length % step == 0:
                if self.is_repeated(s, length, step):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()

    r = s.repeatedSubstringPattern("")
    assert r is False

    r = s.repeatedSubstringPattern("a")
    assert r is False

    r = s.repeatedSubstringPattern("ab")
    assert r is False

    r = s.repeatedSubstringPattern("aa")
    assert r is True

    r = s.repeatedSubstringPattern("abc")
    assert r is False

    r = s.repeatedSubstringPattern("abcab")
    assert r is False

    r = s.repeatedSubstringPattern("abcabc")
    assert r is True

    r = s.repeatedSubstringPattern("abcabcabc")
    assert r is True

    r = s.repeatedSubstringPattern("ababab")
    assert r is True

    r = s.repeatedSubstringPattern("aabaaba")
    assert r is False
