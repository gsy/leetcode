class Solution:
    def search(self, A, target):
        length = len(A)
        if length == 0 or A[-1] <= target:
            return False, None

        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] > target:
                right = mid
            elif A[mid] <= target:
                left = mid + 1

        return True, left

    def advantageCount(self, A, B):
        A = sorted(A)
        length = len(A)
        result = []

        for j in range(length):
            # 找到一个比 B[i] 大的数，但是要最小
            match, i = self.search(A, B[j])
            if match:
                result.append(A.pop(i))
            else:
                result.append(A.pop(0))

        return result
