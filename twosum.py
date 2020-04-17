# -*- coding: utf-8 -*-


class Solution:
    def binarySearch(self, numbers, target, start, end):
        left, right = start, end
        while left <= right:
            middle = int((left + right) / 2)
            if numbers[middle] == target:
                return middle
            elif numbers[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return None

    def twoSum(self, numbers, target):
        for index, number in enumerate(numbers):
            wanted = target - number
            if wanted < number:
                break
            found = self.binarySearch(numbers, target=wanted, start=index+1, end=len(numbers) - 1)
            if found is not None:
                return [index+1, found+1]

        return []


if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([2, 7, 11, 15], 9)
    print(r)

    r = s.twoSum([2, 7, 11, 15], 8)
    print(r)

    r = s.twoSum([2, 7, 11, 15], 17)
    print(r)

    r = s.twoSum([2, 7, 9, 11, 15], 17)
    print(r)

    r = s.twoSum([2, 7, 9, 11, 15], 9)
    print(r)

    r = s.twoSum([2, 7, 9, 11, 15], 8)
    print(r)

    r = s.twoSum([1,2,3,4,4,9,56,90], 8)
    print(r)
