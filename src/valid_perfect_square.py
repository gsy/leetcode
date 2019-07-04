# -*- coding: utf-8 -*-

class Solution:
    def isPerfectSquare(self, num):
        if num in (0, 1):
            return True
        elif num <= 3:
            return False

        left, right = 1, num / 2
        while left <= right:
            middle = int((left + right) / 2)
            target = middle * middle
            if target == num:
                return True
            elif target > num:
                right = middle - 1
            else:
                left = middle + 1

        return False


if __name__ == "__main__":
    s = Solution()
    r = s.isPerfectSquare(0)
    assert r is True

    r = s.isPerfectSquare(1)
    assert r is True

    r = s.isPerfectSquare(2)
    assert r is False

    r = s.isPerfectSquare(3)
    assert r is False

    r = s.isPerfectSquare(4)
    assert r is True

    r = s.isPerfectSquare(16)
    assert r is True

    r = s.isPerfectSquare(9)
    assert r is True

    r = s.isPerfectSquare(8)
    assert r is False

    r = s.isPerfectSquare(15)
    assert r is False
