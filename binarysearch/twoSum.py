class Solution:
    def twoSum(self, numbers, target):
        length = len(numbers)

        for i in range(length):
            remain = target - numbers[i]

            left, right = i + 1, length - 1

            while left <= right:
                j = (left + right) // 2
                mid = numbers[j]
                if mid == remain:
                    return [i+1, j+1]
                elif mid > remain:
                    right = j - 1
                else:
                    left = j + 1
        return []
