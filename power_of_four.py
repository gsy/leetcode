# -*- coding: utf-8 -*-


class Solution:
    def isPowerOfFour(self, num):
        if num == 1:
            return True

        start = 4
        while start <= num:
            if start == num:
                return True
            else:
                start = start << 2
        return False

if __name__ == "__main__":
    s = Solution()
    r = s.isPowerOfFour(1)
    assert r is True

    r = s.isPowerOfFour(5)
    assert r is False

    r = s.isPowerOfFour(16)
    assert r is True

    r = s.isPowerOfFour(4)
    assert r is True

    r = s.isPowerOfFour(7)
    assert r is False
