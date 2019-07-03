# -*- coding: utf-8 -*-


class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []

        result = []
        nodes = [root]
        visited = {}
        while nodes:
            current = nodes[-1]
            print(f"current {current.val}, nodes {nodes}")
            if current.left and (current.left not in visited):
                nodes.append(current.left)
                visited[current] = 1
            else:
                visited[current] = 1
                current = nodes.pop()
                result.append(current.val)
                if current.right and (current.right not in visited):
                    nodes.append(current.right)

        return result
