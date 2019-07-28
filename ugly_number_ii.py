# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        calculated = [1, 2, 3, 4, 5]
        seen = set(calculated)
        primes = [2, 3, 5]
        index, start = 4, 5
        while index <= 1000:
            start = start + 1
            for prime in primes:
                if start % prime == 0 and int(start / prime) in seen:
                    calculated.append(start)
                    seen.add(start)
                    index = index + 1
                    break
        self.calculated = calculated

    def nthUglyNumber(self, n):
        # calculated = [1, 2, 3, 4, 5]
        # primes = [2, 3, 5]
        # index, start = 4, 5
        # while index <= n:
        #     start = start + 1
        #     for prime in primes:
        #         if start % prime == 0 and int(start / prime) in calculated:
        #             calculated.append(start)
        #             index = index + 1
        #             break
        return self.calculated[n-1]


if __name__ == "__main__":
    s = Solution()
    r = s.nthUglyNumber(1)
    assert r == 1

    r = s.nthUglyNumber(2)
    assert r == 2

    r = s.nthUglyNumber(3)
    assert r == 3

    r = s.nthUglyNumber(4)
    assert r == 4

    r = s.nthUglyNumber(5)
    assert r == 5

    r = s.nthUglyNumber(6)
    assert r == 6

    r = s.nthUglyNumber(7)
    assert r == 8

    r = s.nthUglyNumber(8)
    assert r == 9

    r = s.nthUglyNumber(9)
    assert r == 10

    r = s.nthUglyNumber(10)
    assert r == 12

    r = s.nthUglyNumber(12)
    assert r == 16

    r = s.nthUglyNumber(19)
    assert r == 32

    r = s.nthUglyNumber(186)
    print(r)
    assert r == 12288
