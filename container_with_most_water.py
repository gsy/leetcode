__author__ = 'guang'

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        >>> s = Solution()
        >>> s.maxArea([1, 4, 7, 8])
        8
        >>> s.maxArea([])
        0
        >>> s.maxArea([1])
        0
        >>> s.maxArea([1,10])
        1
        """
        if len(height) == 0:
            return 0

        i, j = 0, len(height) - 1
        result = 0
        while i < j:
            h = min(height[i], height[j])
            width = j - i
            water = h * width
            if water > result:
                result = water

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return result

