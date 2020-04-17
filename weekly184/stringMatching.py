class Solution:
    def isSubstring(self, a, b):
        return a in b

    def stringMatching(self, words):
        N = len(words)
        result = []
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                elif self.isSubstring(words[i], words[j]):
                    result.append(words[i])
                    break

        return result
