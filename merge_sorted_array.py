__author__ = 'guang'

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        >>> s = Solution()
        >>> nums1 = [1, 4, 7, None, None, None]
        >>> s.merge(nums1, 3, [2, 5, 6], 3)
        >>> nums1
        [1, 2, 4, 5, 6, 7]
        >>> nums1 = [None, None, None]
        >>> s.merge(nums1, 0, [1, 2, 3], 3)
        >>> nums1
        [1, 2, 3]
        >>> nums1 = [2,0]
        >>> s.merge(nums1, 1, [1], 1)
        >>> nums1
        [1, 2]
        """
        if n == 0:
            return
        elif m == 0:
            for i, x in enumerate(nums2):
                nums1[i] = x
            return

        i = m - 1
        j = n - 1
        end = m + n - 1

        while end >= 0:
            if i < 0:
                nums1[end] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[end] = nums1[i]
                i -= 1
            else:
                if nums1[i] >= nums2[j]:
                    nums1[end] = nums1[i]
                    i -= 1
                else:
                    nums1[end] = nums2[j]
                    j -= 1
            end -= 1




