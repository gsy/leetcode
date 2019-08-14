# -*- coding: utf-8 -*-


class Solution:
    def is_neigbor(self, i, j, length):
        if i == 0 and j == length - 1:
            return True
        elif j - i == 1:
            return True
        return False

    def rob(self, nums):
        money, result, length = [], 0, len(nums)
        for i, num in enumerate(nums):
            if i <= 1:
                current = num
                money.append(num)
            elif i == 2:
                if self.is_neigbor(i - 2, i, length):
                    current = num
                else:
                    current = num + money[i-2]
            else:
                prev1 = money[i-2]
                if self.is_neigbor(i - 3, i, length):
                    prev2 = 0
                else:
                    prev2 = money[i-3]
                current = max(prev1, prev2) + num
                money.append(current)
            if current > result:
                result = current

        print(money)
        return result

if __name__ == "__main__":
    s = Solution()
    r = s.rob([2, 3, 2])
    print(r)
    assert r == 3

    r = s.rob([1, 2, 3, 1])
    print(r)
    assert r == 4

    r = s.rob([1, 2, 3, 10])
    assert r == 12

    r = s.rob([1, 2, 15, 23, 10])
    print(r)
    assert r == 26
