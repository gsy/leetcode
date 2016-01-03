__author__ = 'guang'

from bst import TreeNode
import array_to_bst

class Solution(object):
    def find_smaller(self, node, x):
        """
        >>> s = Solution()
        >>> tree = TreeNode(None).from_string("9,6,10,4,7,8,17")
        >>> found, n = s.find_smaller(tree.right, tree.val)
        >>> found == True and n.val == 8
        True
        """
        if node is None:
            return False, node

        if node.val < x:
            return True, node

        found, n = self.find_smaller(node.left, x)
        if found:
            return True, n
        else:
            return self.find_smaller(node.right, x)

    def find_greater(self, node, x):
        """
        >>> s = Solution()
        >>> tree = TreeNode(None).from_string("9,6,10,4,7,8,17")
        >>> found, n = s.find_greater(tree.left, tree.val)
        >>> found
        False
        """
        if node is None:
            return False, node

        if node.val > x:
            return True, node

        found, n = self.find_greater(node.left, x)
        if found:
            return True, n
        else:
            return self.find_greater(node.right, x)

    def swap(self, n1, n2):
        """
        >>> s = Solution()
        >>> tree = TreeNode(None).from_string("9,6,10,4,7,8,17")
        >>> root = tree
        >>> p2 = root.right
        >>> n2 = p2.left
        >>> s.swap(root, n2)
        >>> tree.show()
        """
        n1.val, n2.val = n2.val, n1.val

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        >>> s = Solution()
        >>> tree = TreeNode(None).from_string("9,6,10,4,7,8,17")
        >>> s.recoverTree(tree)
        >>> tree.val == 8 and tree.right.left.val == 9
        True
        >>> tree = TreeNode(None).from_string("8,9,10,4,7,6,17")
        >>> s.recoverTree(tree)
        >>> tree.val == 8 and tree.left.val == 6 and tree.right.left.val == 9
        True
        >>> tree = TreeNode(None).from_string("8,7,10,4,6,9,17")
        >>> s.recoverTree(tree)
        >>> tree.val == 8 and tree.left.val == 6 and tree.left.right.val == 7
        True
        >>> tree = TreeNode(None).from_string("3,#,2,#,1")
        >>> s.recoverTree(tree)
        >>> tree.val == 1 and tree.right.val == 2 and tree.right.right.val == 3
        True
        >>> tree = TreeNode(None).from_string("4,#,2,#,3,#,1")
        >>> s.recoverTree(tree)
        >>> tree.show()
        """
        if root is None:
            return

        found1, smaller = self.find_smaller(root.right, root.val)
        found2, greater = self.find_greater(root.left, root.val)

        if found1 and found2:
            self.swap(smaller, greater)
        elif found1:
            result, smallest = self.find_smaller(smaller.right, smaller.val)
            if result:
                self.swap(root, smallest)
            else:
                self.swap(root, smaller)
        elif found2:
            result, greatest = self.find_greater(greater.left, greater.val)
            if result:
                self.swap(root, greatest)
            else:
                self.swap(root, greater)
        else:
            self.recoverTree(root.left)
            self.recoverTree(root.right)
