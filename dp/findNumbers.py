class Solution:
    def getDigits(self, num):
        n = num
        count = 0
        while n > 0:
            n = int(n / 10)
            count = count + 1

        return count

    def findNumbers(self, nums):
        result = 0
        for num in nums:
            digits = self.getDigits(num)
            if digits % 2 == 0:
                result = result + 1
        return result
