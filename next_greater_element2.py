# -*- coding: utf-8 -*-


class Solution:
    def nextGreaterElements(self, nums):
        length = len(nums)
        if length == 0:
            return []

        result = []
        pending = []
        for i, current in enumerate(nums):
            found = False
            for j in range(1, length):
                index = (i + j) % length
                right = nums[index]
                if right > current:
                    found = True
                    result.append(right)
                    break
                else:
                    pending.append(right)
            if not found:
                result.append(-1)

        return result


if __name__ == '__main__':
    s = Solution()

    r = s.nextGreaterElements([1, 2, 1])
    print(r)
    assert r == [2, -1, 2]

    r = s.nextGreaterElements([4, 1, 2, 4])
    print(r)
    assert r == [-1, 2, 4, -1]

    r = s.nextGreaterElements([1, 2, 3, 4, 1])
    print(r)
    assert r == [2, 3, 4, -1, 2]

    r = s.nextGreaterElements([7, 6, 5, 4, 3, 2, 1, 7])
    print(r)
    assert r == [-1, 7, 7, 7, 7, 7, 7, -1]

    r = s.nextGreaterElements([5, 4, 3, 2, 1])
    assert r == [-1, 5, 5, 5, 5]

    r = s.nextGreaterElements([4, 1, 2])
    assert r == [-1, 2, 4]

    r = s.nextGreaterElements([2, 4, 3, 1])
    print(r)
    assert r == [4, -1, 4, 2]

    r = s.nextGreaterElements([100, 1, 11, 1, 120, 111, 123, 1, -1, -100])
    print(r)
    assert r == [120, 11, 120, 120, 123, 123, -1, 100, 100, 100]
