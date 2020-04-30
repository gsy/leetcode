class Solution:
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i = i + 1
                j = j - 1
        return True

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        A = [[(0, 0) for i in range(length)] for j in range(length)]

        if length == 0:
            return ""

        # 记下来位置
        for step in range(length):
            for i in range(length-step):
                j = i + step
                if step == 0:
                    A[i][j] = (i, j)
                    continue

                if self.isPalindrome(s[i:j+1]):
                    A[i][j] = (i, j)
                else:
                    x1, y1 = A[i+1][j]
                    x2, y2 = A[i][j-1]

                    l1 = abs(x1 - y1)
                    l2 = abs(x2 - y2)

                    if l1 >= l2:
                        A[i][j] = (x1, y1)
                    else:
                        A[i][j] = (x2, y2)

        start, end = A[0][length-1]
        return s[start: end+1]
