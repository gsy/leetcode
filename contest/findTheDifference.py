class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1, sum2 = 0, 0
        for char in s:
            sum1 += ord(char) - ord('a')

        for char in t:
            sum2 += ord(char) - ord('a')

        return chr((sum2 - sum1) + ord('a'))
