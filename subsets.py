# -*- coding: utf-8 -*-


class Solution:
    def subsets(self, nums):
        length = len(nums)
        if length == 0:
            return []

        elif length == 1:
            return [nums, []]

        else:
            result = []
            for subset in self.subsets(nums[1:]):
                result.append(subset + [nums[0]])
                result.append(subset)
            return result


if __name__ == "__main__":
    s = Solution()
    r = s.subsets([1])
    print(r)
    assert r == [[1], []]

    r = s.subsets([1, 2])
    print(r)
    # assert set(r) == set([[], [1], [2], [1, 2]])

    r = s.subsets([1, 2, 3])
    print(r)
    # assert r == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
