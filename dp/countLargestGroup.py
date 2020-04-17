class Solution:
    def getDigits(self, num):
        result = 0
        while num > 0:
            d = num % 10
            result = result + d
            num = int(num / 10)
        return result

    def countLargestGroup(self, n):
        count = {}
        max_digits = 0
        for i in range(1, n+1):
            digits = self.getDigits(i)
            if digits in count:
                ls = count[digits]
                ls.append(i)
            else:
                count[digits] = [i]
            if len(count[digits]) > max_digits:
                max_digits = len(count[digits])

        result = 0
        for key, values in count.items():
            if len(values) == max_digits:
                result = result + 1

        return result
