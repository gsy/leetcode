__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        >>> s = Solution()
        >>> s.postorderTraversal(None)
        []
        >>> s.postorderTraversal(TreeNode(2))
        [2]
        >>> tree = TreeNode(None).from_string("1,2,3")
        >>> s.postorderTraversal(tree)
        [2, 3, 1]
        >>> tree = TreeNode(None).from_string("1,#,3")
        >>> s.postorderTraversal(tree)
        [3, 1]
        >>> tree = TreeNode(None).from_string("1,#,2,3")
        >>> s.postorderTraversal(tree)
        [3, 2, 1]
        """
        if root is None:
            return []

        result = []
        stack = [root]
        scan_left, scan_right = False, False
        while stack:
            node = stack[-1]
            if node.left and not scan_left:
                stack.append(node.left)
                scan_left = True
            elif node.right and not scan_right:
                stack.append(node.right)
                scan_left = True
                scan_right = True
            else:
                last = stack.pop()
                result.append(last.val)
                if scan_left and scan_right:
                    parent = stack.pop()
                    result.append(parent.val)
                    scan_left, scan_right = False, False

        return result
