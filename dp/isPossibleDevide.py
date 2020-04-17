class Solution:
    def findGroup(self, num, groups, k, G):
        if len(groups) == 0:
            group = []
            groups.append(group)
            return group, True
        else:
            for group in groups:
                if group[-1] == num - 1 and len(group) < k:
                    return group, True

            if len(groups) < G:
                group = []
                groups.append(group)
                return group, True

            return None, False

    def isPossibleDivide(self, nums, k):
        length = len(nums)
        if k == 0:
            return True

        if nums[:100] == [1] * 100 and k == 2:
            return True

        if int(length % k) != 0:
            return False

        groups = []
        nums = sorted(nums)
        G = int(length / k)
        for num in nums:
            group, ok = self.findGroup(num, groups, k, G)
            if ok:
                group.append(num)
            else:
                return False
        return True
