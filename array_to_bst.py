__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        >>> s = Solution()
        >>> tree = s.sortedArrayToBST([1, 2, 3])
        >>> tree.show()
        2
         left: 1
         right: 3
        >>> tree = s.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 9, 10])
        >>> tree.show()
        """

        if not nums:
            return None

        length = len(nums)
        if length == 1:
            return TreeNode(nums[0])
        elif length == 2:
            root = TreeNode(nums[1])
            left = TreeNode(nums[0])
            root.left = left
            return root
        elif length == 3:
            root = TreeNode(nums[1])
            left = TreeNode(nums[0])
            right = TreeNode(nums[2])
            root.left = left
            root.right = right
            return root
        else:
            middle = length / 2
            root = TreeNode(nums[middle])
            left = self.sortedArrayToBST(nums[:middle])
            right = self.sortedArrayToBST(nums[middle+1:])
            root.left = left
            root.right = right
            return root
