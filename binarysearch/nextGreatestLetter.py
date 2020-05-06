class Solution:
    def nextGreatestLetter(self, letters, target):
        nums = [ord(letter) - ord('a') for letter in letters]
        x = ord(target) - ord('a')
        length = len(letters)

        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= x:
                left = mid + 1
            else:
                right = mid

        current = ord(letters[right]) - ord('a')
        if current > x:
            return letters[right]

        return letters[(right+1) % length]
