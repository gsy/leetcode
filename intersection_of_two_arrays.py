# -*- coding: utf-8 -*-


class Solution:
    def intersect(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 == 0 or len2 == 0:
            return []

        if len1 > len2:
            nums1, nums2 = nums2, nums1

        used = {}
        result = []
        for x in nums1:
            found = False
            for index, y in enumerate(nums2):
                if x == y and used.get(index, False) is False:
                    found = True
                    break
            if found:
                result.append(x)
                used[index] = True

        return result
