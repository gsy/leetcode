class Solution:
    def isPalindrome(self, word):
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i = i + 1
            j = j - 1
        return True

    def backtrack(self, s, path, result):
        if len(s) == 0:
            result.append(path)

        for i in range(1, len(s)+1):
            sub = s[:i]
            if self.isPalindrome(sub):
                self.backtrack(s[i:], path + [sub], result)

    def partition(self, s):
        path, result = [], []
        self.backtrack(s, path, result)
        return result
