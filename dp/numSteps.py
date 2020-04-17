class Solution:
    def binaryAddOne(self, s):
        length = len(s)
        carry = 0
        result = ""
        for i in range(length-1, -1, -1):
            digit = int(s[i])
            if i == length - 1:
                tmp = digit + 1 + carry
            else:
                tmp = digit + carry

            if tmp >= 2:
                carry = int(tmp / 2)
                tmp = tmp % 2
            else:
                carry = 0

            result = str(tmp) + result
        if carry:
            result = str(carry) + result
        return result

    def numSteps(self, s):
        steps = 0
        while s != "1":
            if s[-1] == '1':
                s = self.binaryAddOne(s)
            else:
                s = s[:-1]
            # print(s)
            steps += 1

        return steps
