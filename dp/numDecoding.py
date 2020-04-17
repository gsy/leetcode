class Solution:
    def numDecodings(self, s):
        length = len(s)
        if length <= 1:
            return 1

        A = [1] * length

        for i in range(length):
            if i == 0:
                A[i] = 1
            else:
                step = 1
                while True:
                    if int(s[length - i - 1: length - i - 1 + step]) < 26 and length - i - 1 + step <= length:
                        A[i] += A[i - step] + 1
                        step = step + 1
                    else:
                        break

        print(A)

        return A[length - 1]
