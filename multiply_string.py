class Solution:
    def add(self, num1, num2):
        a = num1[::-1]
        b = num2[::-1]
        if len(a) > len(b):
            a, b = b, a

        common = min(len(a), len(b))
        c = []
        carry = 0
        for i in range(common):
            x = a[i]
            y = b[i]
            result = int(x) + int(y) + carry
            if result >= 10:
                carry = int(result / 10)
                result = result % 10
            else:
                carry = 0
            c.append(str(result))

        for i in range(common, len(b)):
            y = b[i]
            result = int(y) + carry
            if result >= 10:
                carry = int(result / 10)
                result = result % 10
            else:
                carry = 0
            c.append(str(result))
        if carry:
            c.append(str(carry))
        return "".join(c)[::-1]

    def single_multiply(self, num1, a):
        if a == '0':
            return "0"

        if a == '1':
            return num1

        num = num1[::-1]
        carry = 0
        c = []

        for x in num:
            result = int(x) * int(a) + carry
            if result >= 10:
                carry = int(result / 10)
                result = result % 10
            else:
                carry = 0
            c.append(str(result))

        if carry:
            c.append(str(carry))
        return "".join(c)[::-1]

    def multiply(self, num1, num2):
        if len(num2) == 0 or len(num1) == 0:
            return "0"
        if num1 == '0' or num2 == '0':
            return '0'

        n2 = num2[::-1]
        n1 = num1
        result = "0"
        for a in n2:
            result = self.add(result, self.single_multiply(n1, a))
            n1 = n1 + "0"

        return result
