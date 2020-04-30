class Solution:
    def minArray(self, numbers):
        length = len(numbers)
        left, right = 0, length - 1

        while left < right:
            mid = (left + right) // 2

            if (mid-1 >= 0 and numbers[mid-1] > numbers[mid]) and\
               (mid+1 < length and numbers[mid+1] > numbers[mid]):
                return numbers[mid]
            elif numbers[mid] < numbers[left]:
                right = mid
            else:
                left = mid + 1

        return numbers[0]
