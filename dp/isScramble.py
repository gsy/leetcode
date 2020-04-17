class Solution:
    def isScramble(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)

        if len1 != len2:
            return False

        if len1 == 0 and len2 == 0:
            return True

        length = len1
        A = [[[False] * (length + 1) for j in range(length)] for i in range(length)]

        print(length)
        for l in range(1, length+1):
            for i in range(length+1-l):
                for j in range(length+1-l):
                    if l == 1:
                        if s1[i] == s2[j]:
                            A[i][j][l] = True
                    else:
                        flag = False
                        for k in range(1, l):
                            if (A[i][j][k] and A[i+k][j+k][l-k]) or \
                               (A[i][j+(l-k)][k] and A[i+k][j][l-k]):
                                flag = True
                                break

                        A[i][j][l] = flag

        # print(A)
        return A[0][0][length]
