__author__ = 'guang'

class Solution(object):
    def even(self, x):
        return x % 2 == 0

    def leftLength(self, s, x):
        return len([y for y in s if y <= x])

    def middle(self, s):
        length = len(s)
        if self.even(length):
            return s[length/2-1]
        else:
            return s[length/2]

    def leftWithBorder(self, s):
        """
        left side of s, include middle element
        :param s:
        :return:
        >>> s = Solution()
        >>> s.leftWithBorder([1,3,7,8])
        [1, 3]
        >>> s.leftWithBorder([1,2,3,4,5])
        [1, 2, 3]
        >>> s.leftWithBorder([1])
        [1]
        >>> s.leftWithBorder([])
        []
        """
        length = len(s)
        if self.even(length):
            return s[:length/2]
        else:
            return s[:(length/2+1)]


    def left(self, s):
        """
        left side of s, exclude border
        :param s:
        :return:
        >>> s = Solution()
        >>> s.left([1, 3, 7, 8])
        [1, 3]
        >>> s.left([2, 5])
        [2]
        >>> s.left([1,2,5,8,9])
        [1, 2]
        >>> s.left([2,5,8,13,14])
        [2, 5]
        >>> s.left([1,1])
        [1]
        >>> s.left([5])
        []
        """
        return s[:len(s) / 2]

    def right(self, s):
        """
        >>> s = Solution()
        >>> s.right([2, 5])
        [5]
        >>> s.right([1, 2, 5, 8, 9])
        [8, 9]
        >>> s.right([3, 4])
        [4]
        >>> s.right([1, 1])
        [1]
        >>> s.right([1])
        []
        >>> s.right([1,3])
        [3]
        """
        length = len(s)
        if self.even(length):
            return s[length/2:]
        else:
            return s[(length/2+1):]

    def median(self, s):
        """
        >>> s = Solution()
        >>> s.median([5])
        5
        """
        length = len(s)
        if self.even(length):
            return (s[length/2 - 1] + s[length/2]) / 2.0
        else:
            return s[length/2]

    def less_than_middle(self, s):
        length = len(s)
        if self.even(length):
            return length / 2
        else:
            return length / 2 + 1

    def kth(self, s1, s2, k):
        """
        The Kth minimum value in s1 and s2, binary search
        :param s1:
        :param s2:
        :param k:
        :return:
        >>> s = Solution()
        >>> s.kth([], [], 3)
        0
        >>> s.kth([], [1,2,3], 3)
        3
        >>> s.kth([1,2,3], [], 2)
        2
        >>> s.kth([1, 3], [5], 2)
        3
        >>> s.kth([1, 3], [5], 3)
        5
        >>> s.kth([1], [1], 1)
        1
        >>> s.kth([1], [1], 2)
        1
        >>> s.kth([1], [2], 2)
        2
        >>> s.kth([1,1], [1,2], 1)
        1
        >>> s.kth([1,1], [1,2], 2)
        1
        >>> s.kth([1,1], [1,2], 3)
        1
        >>> s.kth([1,1], [1,2], 4)
        2
        >>> s.kth([1], [2,3,4], 2)
        2
        >>> s.kth([1], [2,3,4], 3)
        3
        >>> s.kth([1,2,3,4], [5,6,7,8,9,10], 5)
        5
        >>> s.kth([1,2,3,4], [5,6,7,8,9,10], 6)
        6
        >>> s.kth([], [1, 1], 2)
        1
        >>> s.kth([1], [1,1,1,1], 2)
        1
        >>> s.kth([1,3,7,8], [2,5], 3)
        3
        >>> s.kth([1,3,7,8], [2,5], 4)
        5
        >>> s.kth([2,5,8,13,14], [1,5,7], 4)
        5
        """
        if s1 and s2:
            if k == 1:
                return min(s1[0], s2[0])

            half_length = (len(s1) + len(s2)) / 2
            x = self.middle(s1)
            y = self.middle(s2)
            if k < half_length:
                if x >= y:
                    return self.kth(self.left(s1), s2, k)
                else:
                    return self.kth(s1, self.left(s2), k)
            elif k == half_length:
                if x > y:
                    return self.kth(self.left(s1), s2, k)
                elif x == y:
                    return x
                else:
                    return self.kth(s1, self.left(s2), k)
            else:
                if x <= y:
                    return self.kth(self.right(s1), s2, k-len(self.leftWithBorder(s1)))
                else:
                    return self.kth(s1, self.right(s2), k-len(self.leftWithBorder(s2)))

        elif s1:
            return s1[k-1]
        elif s2:
            return s2[k-1]
        else:
            return 0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        >>> s = Solution()
        >>> nums1 = [1,3,7,8]
        >>> nums2 = [2,5]
        >>> s.findMedianSortedArrays(nums1, nums2)
        4.0
        >>> nums1 = [1,2,5,8,9]
        >>> nums2 = [3,4]
        >>> s.findMedianSortedArrays(nums1, nums2)
        4
        >>> nums1 = [2,5,8,13,14]
        >>> nums2 = [1,5,7]
        >>> s.findMedianSortedArrays(nums1, nums2)
        6.0
        >>> s.findMedianSortedArrays([], [1])
        1
        >>> s.findMedianSortedArrays([], [])
        0.0
        >>> s.findMedianSortedArrays([1,1], [1,1])
        1.0
        >>> s.findMedianSortedArrays([1,1], [2,3])
        1.5
        >>> s.findMedianSortedArrays([1,1,1,1], [1,2])
        1.0
        >>> s.findMedianSortedArrays([1], [2,3,4])
        2.5
        >>> s.findMedianSortedArrays([1,1,1], [1,1,1])
        1.0
        """
        total = len(nums1) + len(nums2)
        if self.even(total):
            k1 = total / 2
            k2 = total / 2 + 1
            return (self.kth(nums1, nums2, k1) + self.kth(nums1, nums2, k2)) / 2.0
        else:
            k = total / 2 + 1
            return self.kth(nums1, nums2, k)
