# -*- coding: utf-8 -*-


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        length2 = len(nums2)
        if length2 == 0:
            return []

        mapping = {}
        prev = nums2[0]
        pending = []
        for i in range(1, length2):
            current = nums2[i]

            for x in pending:
                if current > x:
                    mapping[x] = current
            pending = [x for x in pending if x > current]

            if current > prev:
                mapping[prev] = current
            else:
                pending.append(prev)
            prev = current

        result = []
        for x in nums1:
            if x in mapping:
                result.append(mapping[x])
            else:
                result.append(-1)

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
    print(r)
    assert r == [-1, 3, -1]

    r = s.nextGreaterElement([2, 4], [1, 2, 3, 4])
    print(r)
    assert r == [3, -1]

    r = s.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])
    print(r)
    assert r == [7, 7, 7, 7, 7]
