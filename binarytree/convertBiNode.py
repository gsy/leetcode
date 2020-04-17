
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
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        if root.left is None and root.right is None:
            return root

        elif root.left is None:
            root.right = self.convertBiNode(root.right)
            return root

        elif root.right is None:
            new_root = self.convertBiNode(root.left)
            # root has the maximum value
            rightmost = new_root
            while rightmost:
                if rightmost.right is None:
                    break
                else:
                    rightmost = rightmost.right

            root.left = None
            rightmost.right = root
            return new_root

        else:
            new_root = self.convertBiNode(root.left)
            new_right = self.convertBiNode(root.right)
            # root has the maximum value
            rightmost = new_root
            while rightmost:
                if rightmost.right is None:
                    break
                else:
                    rightmost = rightmost.right

            root.left = None
            rightmost.right = root
            rightmost.right.right = new_right
            return new_root


if __name__ == '__main__':
    s = Solution()
    node = TreeNode(4)
    node.left = TreeNode(2)
    node.right = TreeNode(5)
    node.left.left = TreeNode(1)
    node.left.right = TreeNode(3)
    node.left.left.left = TreeNode(0)
    node.right.right = TreeNode(6)
    print(node.string())
    result = s.convertBiNode(node)
    print(result.string())
