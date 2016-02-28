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
        >>> root = TreeNode(None).from_string("6,2,8,0,4,7,9,#,#,3,5")
        >>> p = root.left
        >>> q = root.right
        >>> s.lowestCommonAncestor(root, p, q).val
        6
        >>> p = root.left
        >>> q = root.left.right
        >>> s.lowestCommonAncestor(root, p, q).val
        2

        >>> root = None
        >>> p = None
        >>> q = None
        >>> s.lowestCommonAncestor(root, p, q)

        >>> root = TreeNode(None).from_string("10,6,12,2,7,11,15,#,#,#,8")
        >>> p = root.left
        >>> q = root.right
        >>> s.lowestCommonAncestor(root, p, q).val
        10
        >>> root = TreeNode(None).from_string("10,6,12,2,7,11,15,#,#,#,8")
        >>> p = root.left
        >>> q = root.left.left
        >>> s.lowestCommonAncestor(root, p, q).val
        6
        >>> root = TreeNode(None).from_string("10,6,12,2,7,11,15,1,3,#,8")
        >>> p = root.left.left
        >>> q = root.left.left.right
        >>> s.lowestCommonAncestor(root, p, q).val
        2
        """
        if root is None:
            return None

        ancestors_of_p = self.ancestors(root, p)

        for ancestor in ancestors_of_p:
            if ancestor is q:
                return ancestor

            if p.val < ancestor.val < q.val or p.val > ancestor.val > q.val:
                return ancestor

        return ancestors_of_p[-1]
