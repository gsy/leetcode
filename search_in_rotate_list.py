class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        >>> s = Solution()
        >>> s.search([4, 5, 6, 7, 0, 1, 2], 4)
        0
        >>> s.search([4, 5, 6, 7, 0, 1, 2], 2)
        6
        >>> s.search([4, 5, 6, 7, 0, 1, 2], 3)
        -1
        >>> s.search([8, 9, 11, 1, 4, 5, 7], 11)
        2
        >>> s.search([8, 9, 11, 1, 4, 5, 7], 5)
        5
        >>> s.search([8, 9, 11, 1, 4, 5, 7], 0)
        -1
        >>> s.search([8, 9, 11, 1, 4, 5, 7], 8)
        0
        >>> s.search([8, 9, 11, 1, 4, 5, 7], 7)
        6
        >>> s.search([4,5,6,7,8,1,2,3], 8)
        4
        >>> s.search([4,5,6,7,8,1,2,3], 3)
        7
        """
        length = len(nums)
        if length < 1:
            return -1

        left, right = 0, length - 1
        while left <= right:
            index = (left + right) / 2
            middle = nums[index]
            if middle == target:
                return index
            elif target < middle:
                if nums[right] <= nums[left] <= middle:
                    if target >= nums[left]:
                        right = index - 1
                    else:
                        left = index + 1
                else:
                    right = index - 1
            else:
                if middle <= nums[right] <= nums[left]:
                    if target <= nums[right]:
                        left = index + 1
                    else:
                        right = index - 1
                else:
                    left = index + 1

        return -1
