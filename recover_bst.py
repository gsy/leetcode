__author__ = 'guang'

from bst import TreeNode
import array_to_bst

class Solution(object):
    def breath_first_search(self, candidates):
        """
        >>> s = Solution()
        >>> tree = array_to_bst.Solution().sortedArrayToBST([1, 2, 3, 4, 5])
        >>> nodes = s.breath_first_search([tree.left])
        >>> values = [node.val for node in nodes]
        >>> values
        [2, 1]
        """
        for node in candidates:
            if node.left:
                candidates.append(node.left)
            if node.right:
                candidates.append(node.right)

        return candidates

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        left_nodes = self.breath_first_search(root.left)
        right_nodes = self.breath_first_search(root.right)

        greater_in_left = [node for node in left_nodes if node.val > root.val]
        smaller_in_right = [node for node in right_nodes if node.val < root.val]
        greater_length = len(greater_in_left)
        smaller_length = len(smaller_in_right)

        if greater_length == 0:
            self.recoverTree(root.right)
        elif smaller_length == 0:
            self.recoverTree(root.left)
        else:
            if greater_length == 1 and smaller_length == 1:
                # swap(x, y)
                pass
            elif greater_length > 1:
                # swap(root, y)
                pass
            else:
                pass
                # swap(root, x)

