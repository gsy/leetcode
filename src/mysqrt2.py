# -*- coding: utf-8 -*-

class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0

        if x <= 3:
            return 1

        left, right = 1, x
        while left <= right:
            middle = int((left + right) / 2)
            target = middle * middle
            if target == x:
                return middle
            elif target > x:
                right = middle - 1
            else:
                left = middle + 1

        result = middle
        while True:
            target = result * result
            if target < x:
                return result
            else:
                result = result - 1

if __name__ == "__main__":
    s = Solution()
    r = s.mySqrt(8)
    print(r)
    assert r == 2

    r = s.mySqrt(100)
    print(r)

    r = s.mySqrt(9)
    print(r)

    r = s.mySqrt(10)
    print(r)

    r = s.mySqrt(11)
    print(r)

    r = s.mySqrt(12)
    print(r)

    r = s.mySqrt(13)
    print(r)

    r = s.mySqrt(14)
    print(r)

    r = s.mySqrt(15)
    print(r)

    r = s.mySqrt(16)
    print(r)
