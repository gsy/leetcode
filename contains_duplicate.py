__author__ = 'guang'

class Solution(object):
    __author__ = 'guang'

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        >>> s = Solution()
        >>> s.containsNearbyDuplicate([1,2,3,1], 3)
        True
        >>> s.containsNearbyDuplicate([1,2,3,1], 2)
        False
        >>> s.containsNearbyDuplicate([1,2,3,1], 1)
        False
        >>> s.containsNearbyDuplicate([1,2,3,1], 0)
        False
        >>> s.containsNearbyDuplicate([1,2,1], 0)
        False
        """
        length = len(nums)
        last_index = {}

        for i in xrange(length):
            if nums[i] in last_index:
                if i - last_index[nums[i]] <= k:
                    return True

            last_index[nums[i]] = i

        return False
