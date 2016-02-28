from bst import TreeNode

class Solution(object):
    def ancestors(self, root, node):
        """
        :param root:
        :param node:
        :return:
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("3,5,1,6,2,0,8,#,#,7,4")
        >>> node = root.left
        >>> result = [n.val for n in s.ancestors(root, node)]
        >>> result
        [3, 5]
        >>> node = root.left.right.right
        >>> result = [n.val for n in s.ancestors(root, node)]
        >>> result
        [3, 5, 2, 4]
        """
        if root is None:
            return []

        result = [root]
        seen = set([root])
        while result:
            current = result[-1]
            seen.add(current)
            if current is node:
                break
            elif current.left and current.left not in seen:
                result.append(current.left)
            elif current.right and current.right not in seen:
                result.append(current.right)
            else:
                result.pop(-1)

        return result


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        >>> s = Solution()
        >>> root = TreeNode(None).from_string("3,5,1,6,2,0,8,#,#,7,4")
        >>> p = root.left
        >>> q = root.left.right.right
        >>> s.lowestCommonAncestor(root, p, q).val
        5
        >>> p = root.left
        >>> q = root.right.right
        >>> s.lowestCommonAncestor(root, p, q).val
        3
        >>> root = TreeNode(None)
        >>> p = None
        >>> q = None
        >>> s.lowestCommonAncestor(root, p, q)

        """
        if root is None:
            return None

        ancestors_of_p = self.ancestors(root, p)
        ancestors_of_q = self.ancestors(root, q)
        len_p = len(ancestors_of_p)
        len_q = len(ancestors_of_q)

        if len_p < len_q:
            for node in ancestors_of_p[::-1]:
                if node in ancestors_of_q:
                    return node
        else:
            for node in ancestors_of_q[::-1]:
                if node in ancestors_of_p:
                    return node


