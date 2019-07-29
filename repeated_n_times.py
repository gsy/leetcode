# -*- coding: utf-8 -*-

class Solution:
    def repeatedNTimes(self, ls):
        count = {}
        length = len(ls)
        for num in ls:
            count[num] = count.get(num, 0) + 1
            if count[num] >= int(length / 2):
                return num
        return None

if __name__ == "__main__":
    s = Solution()
    r = s.repeatedNTimes([1, 2, 3, 3])
    assert r == 3

    r = s.repeatedNTimes([2, 1, 2, 5, 3, 2])
    assert r == 2

    r = s.repeatedNTimes([5,1,5,2,5,3,5,4])
    assert r == 5
