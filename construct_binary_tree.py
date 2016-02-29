from bst import TreeNode

class Solution(object):
    preorder = []
    inorder = []

    def build_tree_recursive(self, pre_start, pre_end, in_start, in_end):
        if pre_end - pre_start <= 0:
            return None

        if pre_end - pre_start == 1:
            return TreeNode(self.preorder[pre_start])

        val = self.preorder[pre_start]
        root_index = self.inorder.index(val)
        left_length = root_index - in_start

        pre_left_start = pre_start + 1
        pre_left_end = pre_left_start + left_length
        # index out of bound
        pre_right_start = pre_start + 1 + left_length
        pre_right_end = pre_end

        in_left_start = in_start
        in_left_end = in_start + left_length
        # index out of bound
        in_right_start = root_index + 1
        in_right_end = in_end

        root = TreeNode(val)
        left = self.build_tree_recursive(pre_left_start, pre_left_end, in_left_start, in_left_end)
        right = self.build_tree_recursive(pre_right_start, pre_right_end, in_right_start, in_right_end)

        root.left = left
        root.right = right
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        >>> s = Solution()
        >>> preorder = [1]
        >>> inorder = [1]
        >>> root = s.buildTree(preorder, inorder)
        >>> root.val == 1 and root.left is None and root.right is None
        True
        >>> preorder, inorder = [], []
        >>> root = s.buildTree(preorder, inorder)
        >>> root is None
        True
        >>> preorder, inorder = [1,2], [2,1]
        >>> root = s.buildTree(preorder, inorder)
        >>> root.val == 1 and root.left.val == 2 and root.right is None
        True
        >>> preorder, inorder = [1,3], [1,3]
        >>> root = s.buildTree(preorder, inorder)
        >>> root.val == 1 and root.left is None and root.right.val == 3
        True
        >>> preorder, inorder = [1,2,3], [2,1,3]
        >>> root = s.buildTree(preorder, inorder)
        >>> root.val == 1 and root.left.val == 2 and root.right.val == 3
        True
        >>> preorder, inorder = [1,2,4,5,3,6,7], [4,2,5,1,6,3,7]
        >>> root = s.buildTree(preorder, inorder)
        >>> root.show()
        """

        if preorder == inorder == []:
            return None

        len_preorder = len(preorder)
        len_inorder = len(inorder)

        if len_preorder == len_inorder == 1:
            return TreeNode(preorder[0])

        self.preorder = preorder
        self.inorder = inorder

        return self.build_tree_recursive(0, len_preorder, 0, len_inorder)
