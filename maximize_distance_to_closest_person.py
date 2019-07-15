# -*- coding: utf-8 -*-

class Solution:
    def maxDistToClosest(self, seats):
        length = len(seats)
        if length <= 1:
            return 0

        if length == 2:
            return 1

        # 0 -> 1
        # 1 -> 1
        prev, count, result = None, 0, 0
        for index, seat in enumerate(seats):
            if seat == 1:
                if prev is None:
                    result = max(result, count)
                else:
                    result = max(result, int((count + 1) / 2))
                prev = index
                count = 0
            else:
                if prev is None:
                    count = count + 1
                    result = max(result, count)
                else:
                    count = count + 1

        return max(result, count)


if __name__ == "__main__":
    s = Solution()
    r = s.maxDistToClosest([1, 0])
    assert r == 1

    r = s.maxDistToClosest([1, 0, 0])
    assert r == 2

    r = s.maxDistToClosest([0, 1])
    assert r == 1

    r = s.maxDistToClosest([0, 1, 0])
    assert r == 1

    r = s.maxDistToClosest([0, 0, 0, 0, 0, 0, 0, 1])
    assert r == 7

    r = s.maxDistToClosest([1, 0, 0, 0])
    assert r == 3

    r = s.maxDistToClosest([1, 0, 0, 0, 1])
    assert r == 2

    r = s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1])
    assert r == 2
