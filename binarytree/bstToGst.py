# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


acc = 0
class Solution:
    def dfs(self, root):
        global acc
        if root is None:
            return

        if root.right:
            self.dfs(root.right)
        print(f"{root.val}->{root.val+acc, {acc}}")
        root.val = root.val + acc
        acc = root.val

        if root.left:
            self.dfs(root.left)
        return

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 后序遍历：右 -> 中 -> 左
        global acc
        acc = 0
        self.dfs(root)
        return root


if __name__ == '__main__':
    node = TreeNode(4)
    node.left = TreeNode(1)
    node.right = TreeNode(6)
    node.left.left = TreeNode(0)
    node.left.right = TreeNode(2)
    node.left.right.right = TreeNode(3)
    node.right.left = TreeNode(5)
    node.right.right = TreeNode(7)
    node.right.right.right = TreeNode(8)

    s = Solution()
    s.bstToGst(node)
