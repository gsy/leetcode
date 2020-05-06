class Solution:
    def findClosestElements(self, arr, k, x):
        length = len(arr)
        left, right = 0, length-1
        while left < right:
            mid = (left + right) // 2
            if mid == left:
                break

            if arr[mid] <= x:
                left = mid
            else:
                right = mid - 1

        # left 是小于或者等于 target 的数
        # 从 left 开始找 k 个数
        # 不一定选 left
        # print("left", left)
        count = 0
        start, end = left+1, left
        while count < k:
            if start >= 1 and end < length - 1:
                a = abs(arr[start-1] - x)
                b = abs(arr[end+1] - x)
                if a <= b:
                    start = start - 1
                else:
                    end = end + 1
                count += 1
            elif start >= 1:
                start -= 1
                count += 1
            elif end < length - 1:
                end += 1
                count += 1
            else:
                break
        return arr[max(start, 0): end+1]
