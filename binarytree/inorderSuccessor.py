#!/usr/bin/env python3

class Solution:
    def inorderSuccessor(self, root, p):
        if root is None:
            return None

        stack = [root]
        seen = set()

        found = False
        while len(stack) > 0:
            current = stack[-1]
            if current.left is not None and current.left.val not in seen:
                stack.append(current.left)
                continue
            else:
                current = stack.pop(-1)
                seen.add(current.val)
                if found:
                    return current
                if current.val == p.val:
                    found = True

                if current.right is not None and current.right.val not in seen:
                    stack.append(current.right)

        return None
