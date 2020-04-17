# -*- coding: utf-8 -*-


class Solution:
    def findDisappearedNumbers(self, nums):
        length = len(nums)
        count = [0] * (length + 1)
        # 先是全量的，然后删除
        for num in nums:
            count[num] = count[num] + 1

        result = []
        for index, num in enumerate(count):
            if index == 0:
                continue
            if num == 0:
                result.append(index)
        return result

if __name__ == "__main__":
    s = Solution()
    r = s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    print(r)
    assert r == [5, 6]
