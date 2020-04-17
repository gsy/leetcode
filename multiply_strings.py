class Solution(object):
    def multiply_helper(self, x, nums, result):
        carry = 0
        for j in range(len(nums), 0, -1):
            mul = int(x) * int(nums[j-1]) + carry
            carry = mul / 10
            result.append(str(mul % 10))
        if carry != 0:
            result.append(str(carry))
        return ''.join(reversed(result))

    def string_add(self, str1, str2):
        if len(str1) <= 0 or len(str2) <= 0:
            return "0"
        elif int(str1) == 0 and int(str2) == 0:
            return "0"

        result = []
        carry = 0
        len1 = len(str1)
        len2 = len(str2)
        max_length = max(len1, len2)
        for i in range(max_length):
            x = int(str1[len1 - 1 - i]) if i < len(str1) else 0
            y = int(str2[len2 - 1 - i]) if i < len(str2) else 0
            acc = x + y + carry
            result.append(str(acc % 10))
            carry = acc / 10
        if carry != 0:
            result.append(str(carry))

        return ''.join(reversed(result))


    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        count = 0
        result = "0"
        for i in range(len(num1), 0, -1):
            tmp = self.multiply_helper(num1[i-1], num2, ['0' * count])
            count = count + 1
            result = self.string_add(result, tmp)

        return result



if __name__ == "__main__":
    s = Solution()
    num1 = "123"
    num2 = "456"
    r = s.multiply(num1, num2)
    print r
