from bst import TreeNode

class Solution(object):
    inorder = []
    postorder = []

    def build_tree_recursive(self, inorder_start, inorder_end, postorder_start, postorder_end):
        if inorder_end - inorder_start == 0:
            return None

        if inorder_end - inorder_start == 1:
            return TreeNode(self.inorder[inorder_start])

        val = self.postorder[postorder_end - 1]
        root_index = self.inorder.index(val)
        left_length = root_index - inorder_start

        in_left_start = inorder_start
        in_left_end = in_left_start + left_length
        in_right_start = root_index + 1
        in_right_end = inorder_end

        post_left_start = postorder_start
        post_left_end = postorder_start + left_length
        post_right_start = post_left_end
        post_right_end = postorder_end - 1

        root = TreeNode(val)
        left = self.build_tree_recursive(in_left_start, in_left_end, post_left_start, post_left_end)
        right = self.build_tree_recursive(in_right_start, in_right_end, post_right_start, post_right_end)

        root.left = left
        root.right = right
        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        >>> s = Solution()
        >>> inorder = [1]
        >>> postorder = [1]
        >>> root = s.buildTree(inorder, postorder)
        >>> root.val == 1 and root.left is None and root.right is None
        True
        >>> postorder, inorder = [], []
        >>> root = s.buildTree(inorder, postorder)
        >>> root is None
        True
        >>> inorder, postorder = [2,1], [2,1]
        >>> root = s.buildTree(inorder, postorder)
        >>> root.val == 1 and root.left.val == 2 and root.right is None
        True
        >>> postorder, inorder = [3,1], [1,3]
        >>> root = s.buildTree(inorder, postorder)
        >>> root.val == 1 and root.left is None and root.right.val == 3
        True
        >>> postorder, inorder = [2,3,1], [2,1,3]
        >>> root = s.buildTree(inorder, postorder)
        >>> root.val == 1 and root.left.val == 2 and root.right.val == 3
        True
        >>> postorder, inorder = [4,2,3,1], [4,2,1,3]
        >>> root = s.buildTree(inorder, postorder)
        >>> root.show()

        """
        if inorder == postorder == []:
            return None

        if len(postorder) == len(inorder) == 1:
            return TreeNode(inorder[0])

        self.inorder = inorder
        self.postorder = postorder
        length = len(inorder)

        return self.build_tree_recursive(0, length, 0, length)
