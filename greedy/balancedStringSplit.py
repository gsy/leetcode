class Solution:
    def balancedStringSplit(self, s):
        total, left, right, length = 0, 0, 0, len(s)

        for i in range(length):
            if left == right and left > 0:
                total = total + 1
            if s[i] == 'L':
                left = left + 1
            elif s[i] == 'R':
                right = right + 1

        return total + 1
