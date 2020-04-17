class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longest_path(self, root):
        if root is None:
            return 0, 0

        left, right, left_result, right_result = 0, 0, 0, 0
        if root.left is not None:
            tmp_left, left_result = self.longest_path(root.left)
            if root.val == root.left.val:
                left = tmp_left + 1

        if root.right is not None:
            tmp_right, right_result = self.longest_path(root.right)
            if root.val == root.right.val:
                right = tmp_right + 1

        return max(left, right), max(left+right, left_result, right_result)

    def longestUnivaluePath(self, root):
        current, history = self.longest_path(root)
        return max(current, history)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    r = s.longestUnivaluePath(root)
    print(r)
    assert r == 2

    root = TreeNode(1)
    root.left = TreeNode(4)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    r = s.longestUnivaluePath(root)
    print(r)
    assert r == 2

    # [1,null,1,1,1,1,1,1]
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    r = s.longestUnivaluePath(root)
    print(r)
    assert r == 2
