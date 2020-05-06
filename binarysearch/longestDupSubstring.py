# 1. 子串重复出现
# 2. 符合条件的最长的


class Solution:
    def search(self, nums, steps, length):
        base = 26
        modulus = 2**64

        prev = 0
        for i in range(steps):
            prev = (prev * base + nums[i]) % modulus

        seen = {prev}

        aL = pow(base, steps, modulus)
        for start in range(1, length - steps + 1):
            # compute rolling hash in O(1) time
            prev = (prev * base - nums[start - 1] * aL + nums[start + steps - 1]) % modulus

            if prev in seen:
                return True, start

            seen.add(prev)
        return False, 0

    def longestDupSubstring(self, S):
        length = len(S)

        left, right = 0, length-1
        longest = 0
        result = ""
        nums = [ord(S[i]) - ord('a') for i in range(length)]

        while left <= right:
            mid = (left + right) // 2
            # print("left", left, "mid", mid, "right", right)
            found, start = self.search(nums, mid, length)
            print("left", left, "mid", mid, "right", right, "found", found, "start", start, "length", length)
            if found:
                # 找到了，那找更大的
                if mid > longest:
                    longest == mid
                    result = S[start: start+mid]

                left = mid + 1
            else:
                right = mid - 1
        return result
