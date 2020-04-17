class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        length = len(S)
        if length == 0:
            return ""

        left, right = "", ""

        i, j = 0, length - 1
        while i < j:
            while not i.isalpha():
                left = left + S[i]
                i = i + 1
                if i >= j:
                    break

            while not j.isalpha():
                right = S[j] + right
                j = j - 1
                if i > j:
                    break

            if i > j:
                break
            elif i == j:
                left = left + S[i]
                break
            else:
                left = left + S[j]
                right = S[i] + right
                i = i + 1
                j = j - 1
        return left + right
