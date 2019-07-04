def guess(num):
    if num < 6:
        return -1
    elif num == 6:
        return 0
    else:
        return 1


class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n
        while left <= right:
            middle = int((left + right) / 2)
            if guess(middle) == 0:
                return middle
            elif guess(middle) == -1:
                right = middle - 1
            else:
                left = middle + 1

        return 0
