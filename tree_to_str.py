# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t):
        if t is None:
            return "()"

        result = str(t.val) + "({})({})".format(self.tree2str(t.left), self.tree2str(t.right))
        ls = []
        for char in result:
            if char == ')' and ls[-1] == '(':
                ls.pop(-1)
            else:
                ls.append(char)
        return ''.join(ls)


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(4)

    r = s.tree2str(t)
    assert r == '1(2(4))(3)'

    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.right = TreeNode(4)

    r = s.tree2str(t)
    print(r)
    assert r == '1(2()(4))(3)'
