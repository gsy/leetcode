# -*- coding: utf-8 -*-


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last, i, j = m + n - 1, m - 1, n - 1
        while last >= 0:
            if i >= 0 and j >= 0:
                if nums1[i] >= nums2[j]:
                    nums1[last] = nums1[i]
                    i, last = i - 1, last - 1
                else:
                    nums1[last] = nums2[j]
                    j, last = j - 1, last - 1
            elif i >= 0:
                nums1[last] = nums1[i]
                i, last = i - 1, last - 1
            elif j >= 0:
                nums1[last] = nums2[j]
                j, last = j - 1, last - 1


if __name__ == '__main__':
    s = Solution()
    r = s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

    r = s.merge([1, 2, 3, 0, 0, 0], 1, [2, 5, 6], 3)

    r = s.merge([0, 0, 0, 0], 0, [1], 1)
