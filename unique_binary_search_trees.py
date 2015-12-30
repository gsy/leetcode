__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        >>> s = Solution()
        >>> result = s.generateTrees(0)
        >>> not result
        True
        >>> result = s.generateTrees(1)[0]
        >>> result.val and result.left is None and result.right is None
        1
        >>> result = s.generateTrees(2)
        >>> len(result)
        2
        >>> for tree in result: tree.show()

        >>> result = s.generateTrees(3)
        >>> len(result) == 5
        True
        >>> for tree in result: tree.show()

        # >>> result = s.generateTrees(10)
        # >>> len(result) == 16796
        # True
        """
        if n == 0:
            return []

        p = [[None for x in range(n+1)] for y in range(n+1)]
        for i in range(1, n+1):
            p[i][i] = [TreeNode(i)]

        for length in range(1, n):
            for i in range(1, n - length + 1):
                j = i + length
                p[i][j] = []
                for k in range(i, j+1):
                    left, right = [None], [None]
                    if k > i:
                        left = p[i][k-1]
                    if k < j:
                        right = p[k+1][j]

                    for l in left:
                        for r in right:
                            root = TreeNode(k)
                            root.left = l
                            root.right = r
                            p[i][j].append(root)

        return p[1][n]
