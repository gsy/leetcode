# -*- coding: utf-8 -*-

class Solution:
    def nthUglyNumber(self, n):
        current = 1
        time2, time3, time5 = 1, 1, 1
        prev = [0, 1]
        process = ""
        for i in range(1, n):
            current = min(prev[time2] * 2, prev[time3] * 3, prev[time5] * 5)
            if current == prev[time2] * 2:
                time2 = time2 + 1
            if current == prev[time3] * 3:
                time3 = time3 + 1
            if current == prev[time5] * 5:
                time5 = time5 + 1
            prev.append(current)
            # if process:
            #     process = process + "->" + str(current)
            # else:
            #     process = str(current)
            # print(process)
        return current



if __name__ == "__main__":
    s = Solution()
    r = s.nthUglyNumber(1)
    print(r)
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
