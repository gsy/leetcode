class Solution:
    def canPermutePalindrome(self, s):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        odds = 0
        for key, value in count.items():
            if value % 2 == 1:
                odds += 1
            if odds > 1:
                return False
        return True
