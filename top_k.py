# encoding: utf-8
__author__ = 'guang'


class Solution(object):
    def top_k(self, array, k):
        """
        找到数组s中第k大的数，找到返回这个数，找不到返回None
        :param array:
        :return:
        >>> s = Solution()
        >>> s.top_k([1, 2, 5, 8, 3], 3)
        3
        >>> s.top_k([1, 2, 5, 8, 3], 1)
        1
        >>> s.top_k([1, 2, 5, 8, 3], 6)

        >>> s.top_k([1, 2, 5, 8, 3], 4)
        5
        """
        if len(array) == 0 or k < 1:
            return None

        pilot = array[0]
        left, right = [], []
        for index, x in enumerate(array):
            if x < pilot:
                left.append(x)
            elif index != 0:
                right.append(x)

        if len(left) == k - 1:
            return pilot
        elif len(left) >= k:
            return self.top_k(left, k)
        else:
            return self.top_k(right, k-len(left)-1)


