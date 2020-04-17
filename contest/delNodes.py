class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def string(self):
        if self is None:
            return ""

        result = str(self.val)
        if self.left:
            result += self.left.string()
        if self.right:
            result += self.right.string()
        return result


class Solution:
    def delNodes(self, root, to_delete):
        if root is None:
            return []

        result = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop(0)

            print(node.val)
            if node.val in to_delete:
                sub_left = self.delNodes(node.left, to_delete)
                sub_right = self.delNodes(node.right, to_delete)
                return sub_left + sub_right

            if node.left:
                if node.left.val in to_delete:
                    tmp = self.delNodes(node.left, to_delete)
                    result = result + tmp
                    node.left = None
                else:
                    stack.append(node.left)

            if node.right:
                if node.right.val in to_delete:
                    tmp = self.delNodes(node.right, to_delete)
                    result = result + tmp
                    node.right = None
                else:
                    stack.append(node.right)

        result = result + [root]
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    result = s.delNodes(root, [3, 5])
    print(result)
    for item in result:
        print(item.string())
