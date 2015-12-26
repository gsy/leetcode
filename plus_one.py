__author__ = 'guang'


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        >>> s = Solution()
        >>> s.plusOne([1, 2, 3])
        [1, 2, 4]
        >>> s.plusOne([1, 2, 9])
        [1, 3, 0]
        >>> s.plusOne([1])
        [2]
        >>> s.plusOne([9])
        [1, 0]
        >>> s.plusOne([9, 9, 9])
        [1, 0, 0, 0]
        >>> s.plusOne([8, 9 ,9])
        [9, 0, 0]
        """

        length = len(digits)
        if length == 0:
            return []

        left = []
        right = []
        c = 0
        for j in range(length-1, -1, -1):
            x = digits[j]
            if j == length - 1:
                y = x + 1
                c = y / 10
                right.append(y % 10)
            elif c != 0:
                y = x + c
                c = y / 10
                right.append(y % 10)
            else:
                left = digits[:j+1]
                break
        if c != 0:
            right.append(c)

        left.extend(right[::-1])
        return left
















