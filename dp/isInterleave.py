class Solution:
    def isInterleave(self, s1, s2, s3):
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1 + len2 != len3:
            return False

        if len1 == 0 and len2 == 0 and len3 == 0:
            return True
        elif len1 == 0:
            return s2 == s3
        elif len2 == 0:
            return s1 == s3

        A = [[[False] * len2 for i in range(len1)] for k in range(len3)]

        for k in range(len3):
            if k == 0:
                if s1[0] == s3[0] or s2[0] == s3[0]:
                    A[0][0][0] = True
                else:
                    return False
            else:
                for i in range(k+1):
                    flag = False
                    for j in range(k+1-i):
                        if (s1[i] == s3[k] or s2[j] == s3[k]):
                            flag = True
                            break
                        else:
                            return False

        return True
        #             A[k][i][j] = flag

        # print(A)
        # return A[len3-1][len1-1]
