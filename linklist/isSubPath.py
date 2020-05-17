#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubPath(self, head, root):
        if head is None or root is None:
            return False

        seen = set()
        treeNode = root
        values = []

        node, path = head, []
        while node:
            path.append(node.val)
            node = node.next
        pathLength = len(path)

        stack = [root]
        while len(stack) > 0:
            treeNode = stack[-1]
            if treeNode not in seen:
                values.append(treeNode.val)
            seen.add(treeNode)

            if len(values) >= pathLength:
                if values[-pathLength:] == path:
                    return True

            if treeNode.left and treeNode.left not in seen:
                stack.append(treeNode.left)
                continue
            elif treeNode.right and treeNode.right not in seen:
                stack.append(treeNode.right)
                continue
            else:
                stack.pop(-1)
                values.pop(-1)

        return False


if __name__ == '__main__':
        s = Solution()
        ls = ListNode(4)
        ls.next = ListNode(2)
        ls.next.next = ListNode(8)

        root = TreeNode(1)
        root.left = TreeNode(4)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(1)
        root.right.left = TreeNode(2)
        root.right.left.left = TreeNode(6)
        root.right.left.right = TreeNode(8)
        root.right.left.right.left = TreeNode(1)
        root.right.left.right.right = TreeNode(3)

        r = s.isSubPath(ls, root)
        print(r)
