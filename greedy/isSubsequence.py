class Solution:
    def isSubsequence(self, s, t):
        k = 0
        for i in range(len(s)):
            flag = False
            for j in range(k, len(t)):
                if t[j] == s[i]:
                    k = j+1
                    flag = True
                    break
            if not flag:
                return False
        return True
