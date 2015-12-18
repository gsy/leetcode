__author__ = 'guang'

class Solution(object):
    @staticmethod
    def even(x):
        return x % 2 == 0

    @staticmethod
    def median(s):
        """
        >>> Solution.median([1,3,7,8])
        5.0
        >>> Solution.median([3,5])
        4.0
        >>> Solution.median([2,5])
        3.5
        >>> Solution.median([1,2,5,8,9])
        5.0
        >>> Solution.median([3,4])
        3.5
        """
        if len(s) == 0:
            return 0

        length = len(s)
        if Solution.even(length):
            return (s[length / 2 - 1] + s[length / 2]) / 2.0
        else:
            return s[length / 2] * 1.0

    @staticmethod
    def index(s, x):
        """
        index of y, which in s and y <= x, start from 1
        :param s:
        :param x:
        :return:
        >>> s = [1,3,7,8]
        >>> Solution.index(s, 5)
        2
        >>> Solution.index([2, 5], 3.5)
        1
        >>> Solution.index([3,4], 3.5)
        1
        >>> Solution.index([1,5,7], 5)
        2
        >>> Solution.index([1,1], 1.0)
        1
        """
        result = len([y for y in s if y <= x])
        if result == len(s):
            return result - 1
        return result

    @staticmethod
    def left(s, x):
        """
        Element y in s and y < x
        :param s:
        :param x:
        :return:
        >>> Solution.left([1, 3, 7, 8], 5)
        [1, 3]
        >>> Solution.left([2, 5], 3.5)
        [2]
        >>> Solution.left([1,2,5,8,9], 5.0)
        [1, 2]
        >>> Solution.left([2,5,8,13,14], 8.0)
        [2, 5]
        """
        result = [y for y in s if y < x]
        if result:
            return result
        else:
            return [x]

    @staticmethod
    def right(s):
        """
        >>> Solution.right([2, 5], 3.5)
        [5]
        >>> Solution.right([1, 2, 5, 8, 9], 5)
        [8, 9]
        >>> Solution.right([3,4], 3.5)
        [4]
        """



    @staticmethod
    def kth(s1, s2, k):
        """
        The Kth minimum value in s1 and s2
        :param s1:
        :param s2:
        :param k:
        :return:
        >>> Solution.kth([1, 3], [5], 2)
        3
        >>> Solution.kth([1, 3], [5], 3)
        5
        >>> Solution.kth([], [], 3)

        >>> Solution.kth([], [1,2,3], 3)
        3
        >>> Solution.kth([1,2,3], [], 2)
        2
        >>> Solution.kth([1,2,5,8,9], [3,4], 3)
        3
        """
        if s1 and s2:
            if k == 1:
                return min(s1[0], s2[0])
            else:
                if s1[0] < s2[0]:
                    return Solution.kth(s1[1:], s2, k - 1)
                else:
                    return Solution.kth(s1, s2[1:], k - 1)

        elif s1:
            if k == 1:
                return s1[0]
            else:
                return Solution.kth(s1[1:], s2, k - 1)

        elif s2:
            if k == 1:
                return s2[0]
            else:
                return Solution.kth(s1, s2[1:], k - 1)

        else:
            return None

    @staticmethod
    def k(s1, s2, deleted):
        """
        :param s1:
        :param s2:
        :param deleted:
        :return:
        >>> Solution.k([1, 3, 7, 8], [2, 5], 1)
        (2, 3)
        >>> Solution.k([1,2,5,8,9], [3,4], 1)
        (3, 3)
        >>> Solution.k([1,2,5,8,9], [3,4], 1)
        (3, 3)
        >>> Solution.k([1,1], [1,2], 1)
        (1, 2)
        """
        total = len(s1) + len(s2)
        if Solution.even(total):
            return total / 2 - deleted, total / 2 + 1 - deleted
        else:
            return total / 2 + 1 - deleted,  total / 2 + 1 - deleted

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
        4.0
        >>> nums1 = [2,5,8,13,14]
        >>> nums2 = [1,5,7]
        >>> s.findMedianSortedArrays(nums1, nums2)
        6.0
        >>> s.findMedianSortedArrays([], [1])
        1.0
        >>> s.findMedianSortedArrays([], [])
        0
        >>> s.findMedianSortedArrays([1,1], [1,1])
        1.0
        >>> s.findMedianSortedArrays([1,1], [2,3])
        1.5
        >>> s.findMedianSortedArrays([1,1,1,1], [1,2])
        1.0
        """

        if not nums1 and not nums2:
            return 0

        if not nums1:
            return Solution.median(nums2)

        if not nums2:
            return Solution.median(nums1)

        x = Solution.median(nums1)
        y = Solution.median(nums2)

        if x == y:
            return x

        if x < y:
            deleted = Solution.index(nums1, x)
            half_nums1 = Solution.right(nums1)
            half_nums2 = Solution.left(nums2)
        else:
            deleted = Solution.index(nums2, y)
            half_nums1 = Solution.left(nums1, x)
            half_nums2 = Solution.right(nums2, y)

        k1, k2 = self.k(nums1, nums2, deleted)
        return Solution.median([Solution.kth(half_nums1, half_nums2, k1), Solution.kth(half_nums1, half_nums2, k2)])
