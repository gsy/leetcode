# -*- coding: utf-8 -*-


class Solution:
    def to_minutes(self, string):
        hours, minutes = (int(item) for item in string.split(":"))
        return hours * 60 + minutes

    def findMinDifference(self, timePoints):
        # 列表中的时间，先排序，然后循环相减，找出最小值
        minutes = [self.to_minutes(string) for string in timePoints]
        minutes = sorted(minutes)
        # print(minutes)
        minimum, length = None, len(minutes)
        assert length >= 2

        for i in range(length):
            j = (i+1) % length
            diff = (minutes[j] - minutes[i]) % (24 * 60)
            if minimum is None or diff < minimum:
                minimum = diff
        return minimum


if __name__ == '__main__':
    s = Solution()
    r = s.findMinDifference(["23:59", "00:00"])
    assert r == 1

    r = s.findMinDifference(["00:00", "00:01"])
    assert r == 1

    r = s.findMinDifference(["01:00", "00:01"])
    assert r == 59

    r = s.findMinDifference(["12:00", "00:01"])
    print(r)
    assert r == 719
