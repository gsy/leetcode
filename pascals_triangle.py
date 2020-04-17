# -*- coding: utf-8 -*-

class Solution:
    def generate(self, n):
        if n == 0:
            return []

        prev, result = [1], [[1]]
        for i in range(1, n):
            current = []
            for j in range(i+1):
                if j == 0 or j == i:
                    current.append(1)
                else:
                    current.append(prev[j-1]+prev[j])
            result.append(current)
            prev = current
        return result


if __name__ == "__main__":
    s = Solution()
    r = s.generate(5)
    print(r)

    r = s.generate(1)
    print(r)
