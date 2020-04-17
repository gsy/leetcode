# -*- coding: utf-8 -*-

class Solution(object):
    def get_count(self, item):
        return item[1]

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        total = 0
        count = {}
        for candy in candies:
            count[candy] = count.get(candy, 0) + 1
            total = total + 1

        # 每种拿一个，但是只能拿一半
        return min(len(count.keys()), int(total/2))

if __name__ == "__main__":
    s = Solution()
    r = s.distributeCandies([1, 1, 2, 2, 3, 3])
    print(r)
    assert r == 3

    r = s.distributeCandies([1, 1, 2, 3])
    print(r)
    assert r == 2

    r = s.distributeCandies([1, 1, 1, 1, 2, 2, 2, 3, 3, 3])
    print(r)
    assert r == 3
