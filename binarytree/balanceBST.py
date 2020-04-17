class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def string(self):
        result = str(self.val)
        if self.left:
            result = result + self.left.string()
        if self.right:
            result = result + self.right.string()
        return result


class Solution:
    def turnLeft(self, root):
        if root is None or root.right is None:
            return root

        new_root = root.right
        root.right = None
        # leftmost
        leftmost = new_root
        while True:
            if leftmost.left is None:
                break
            else:
                leftmost = leftmost.left
        leftmost.left = root
        return new_root

    def turnRight(self, root):
        if root is None or root.left is None:
            return root

        new_root = root.left
        root.left = None
        # rightmost
        rightmost = new_root
        while True:
            if rightmost.right is None:
                break
            else:
                rightmost = rightmost.right
        rightmost.right = root
        return new_root

    def height(self, root):
        if root is None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        root.left = self.balanceBST(root.left)
        root.right = self.balanceBST(root.right)

        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if abs(left_height - right_height) <= 1:
            return root

        elif left_height > right_height:
            new_root = self.turnRight(root)
            return self.balanceBST(new_root)

        elif left_height < right_height:
            new_root = self.turnLeft(root)
            return self.balanceBST(new_root)


if __name__ == '__main__':
    node = TreeNode(1)
    node.right = TreeNode(2)
    node.right.right = TreeNode(3)
    node.right.right.right = TreeNode(4)

    s = Solution()
    print(node.string())
    result = s.balanceBST(node)
    print(result.string())

    node = TreeNode(19)
    node.left = TreeNode(10)
    node.left.left = TreeNode(4)
    node.left.left.right = TreeNode(5)
    node.left.right = TreeNode(17)
    print(node.string())
    result = s.balanceBST(node)
    print(result.string())
