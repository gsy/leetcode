__author__ = 'guang'

class Solution(object):
    def foo(self, n, p):
        total = 0
        for i in range(1, n+1):
            left = p[i - 1]
            right = p[n - i]
            total += left * right
        return total

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        >>> s = Solution()
        >>> s.numTrees(0)
        1
        >>> s.numTrees(1)
        1
        >>> s.numTrees(2)
        2
        >>> s.numTrees(3)
        5
        >>> s.numTrees(19)
        1767263190
        >>> s.numTrees(10)
        16796
        """
        p = [1, 1]

        for x in range(2, n+1):
            p.append(self.foo(x, p))

        return p[n]



