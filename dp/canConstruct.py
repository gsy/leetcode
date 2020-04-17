class Solution:
    def canConstruct(self, s, k):
        if len(s) == k:
            return True

        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        odd, even_sum = 0, 0
        for key, value in count.items():
            if value % 2 == 1:
                odd = odd + 1
                even_sum = even_sum + (value - 1)
            else:
                even_sum = even_sum + value

        if k >= odd and k <= odd + int(even_sum / 2):
            return True

        return False
