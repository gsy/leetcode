# -*- coding: utf-8 -*-

import collections


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        stack = collections.OrderedDict()
        for num in nums:
            if num in stack:
                return True
            else:
                stack[num] = 1
                if len(stack.keys()) > k:
                    stack.popitem(last=False)
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.containsNearbyDuplicate([1, 2, 3, 1], k=3)
    assert r is True

    r = s.containsNearbyDuplicate([1, 0, 1, 1], k=1)
    assert r is True

    r = s.containsNearbyDuplicate([1, 0, 1, 0, 1], k=1)
    assert r is False

    r = s.containsNearbyDuplicate([1, 0, 1, 0, 1], k=2)
    assert r is True

    r = s.containsNearbyDuplicate([1, 0, 1, 0, 1], k=0)
    assert r is False

    r = s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], k=2)
    assert r is False

    r = s.containsNearbyDuplicate([2, 2], 3)
    assert r is True
