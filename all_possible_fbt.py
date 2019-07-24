# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        three = TreeNode(0)
        three.left = TreeNode(0)
        three.right = TreeNode(0)
        self.mapping = {
            0: [],
            1: [TreeNode(0)],
            2: [],
            3: [three]
        }

    def break_down(self, n, mapping):
        if n in mapping:
            return mapping[n]

        result = []
        for i in range(1, n):
            j = n - i - 1
            left = self.break_down(i, mapping)
            if len(left) > 0:
                right = self.break_down(j, mapping)
                if len(right) > 0:
                    for x in left:
                        for y in right:
                            root = TreeNode(0)
                            root.left = x
                            root.right = y
                            result.append(root)
        if len(result) > 0 and n not in mapping:
            mapping[n] = result
        return result

    def allPossibleFBT(self, n):
        return self.break_down(n, self.mapping)


if __name__ == '__main__':
    s = Solution()
    r = s.allPossibleFBT(4)
    assert r == []

    r = s.allPossibleFBT(5)
    assert len(r) == 2

    r = s.allPossibleFBT(6)
    # print(r)
    assert len(r) == 0

    r = s.allPossibleFBT(7)
    # print(r)
    assert len(r) == 5
    # [[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,null,null,0,0]]

    # [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,0,0,null,null,null,null,0,0]]
