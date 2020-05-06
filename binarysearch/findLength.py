class Solution:

    def search(self, A, B, steps, len1, len2):
        set1 = set()
        str1 = ""

        for i in range(steps):
            str1 = str1 + str(A[i])
        set1.add(str1)

        for i in range(1, len1-steps+1):
            str1 = str1 + str(A[i+steps-1])
            str1 = str1[1:]
            set1.add(str1)
        print("steps", steps, "set", set1)

        str2 = ""
        for j in range(steps):
            str2 = str2 + str(B[j])
        if str2 in set1:
            return True

        for j in range(1, len2-steps+1):
            str2 = str2 + str(B[j+steps-1])
            str2 = str2[1:]
            if str2 in set1:
                return True

        return False

    def findLength(self, A, B):
        len1 = len(A)
        len2 = len(B)
        length = min(len1, len2)

        left, right = 1, length
        result = 0

        while left <= right:
            mid = (left + right) // 2
            # print("left", left, "right", right, "mid", mid)
            # 找到了，找更长的
            if self.search(A, B, mid, len1, len2):
                left = mid + 1
                if mid > result:
                    result = mid
            else:
                right = mid - 1

        return result
