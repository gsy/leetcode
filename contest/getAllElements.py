# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1, root2):
        left_current = root1
        right_current = root2
        stack1 = []
        stack2 = []

        # dfs
        seen1 = []
        seen2 = []

        if left_current:
            stack1.append(left_current)
        if right_current:
            stack2.append(right_current)

        while stack1:
            left_current = stack1[-1]
            while left_current.left and left_current.left.val not in seen1:
                # 往左走
                left_current = left_current.left
                stack1.append(left_current)

            left_current = stack1.pop()
            seen1.append(left_current.val)

            while left_current.right and left_current.right.val not in seen1:
                left_current = left_current.right
                stack1.append(left_current)

        while stack2:
            right_current = stack2[-1]

            while right_current.left and right_current.left.val not in seen2:
                # 往左走
                right_current = right_current.left
                stack2.append(right_current)

            right_current = stack2.pop()
            seen2.append(right_current.val)

            while right_current.right and right_current.right.val not in seen2:
                right_current = right_current.right
                stack2.append(right_current)

        # print(seen1, seen2)
        return sorted(seen1 + seen2)


if __name__ == '__main__':
    left = TreeNode(2)
    left.left = TreeNode(1)
    left.right = TreeNode(4)

    right = TreeNode(1)
    right.left = TreeNode(0)
    right.right = TreeNode(3)

    s = Solution()
    result = s.getAllElements(left, right)
    print("result", result)

    left = TreeNode(0)
    left.left = TreeNode(-10)
    left.right = TreeNode(10)

    right = TreeNode(5)
    right.left = TreeNode(1)
    right.right = TreeNode(7)
    right.left.left = TreeNode(0)
    right.left.right = TreeNode(2)

    s = Solution()
    result = s.getAllElements(left, right)
    print("result", result)

    left = None

    right = TreeNode(5)
    right.left = TreeNode(1)
    right.right = TreeNode(7)
    right.left.left = TreeNode(0)
    right.left.right = TreeNode(2)

    s = Solution()
    result = s.getAllElements(left, right)
    print("result", result)

    left = TreeNode(0)
    left.left = TreeNode(-10)
    left.right = TreeNode(10)

    right = None
    s = Solution()
    result = s.getAllElements(left, right)
    print("result", result)
