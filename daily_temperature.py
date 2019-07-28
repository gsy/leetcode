# -*- coding: utf-8 -*-

class Solution:
    def dailyTemperatures(self, ls):
        length = len(ls)
        right, stack = 1, [0]
        while right < length:
            index = stack[-1]
            while ls[right] > ls[index]:
                stack.pop()
                mapping[index] = right - index
                if len(stack) == 0:
                    break
                else:
                    index = stack[-1]

            stack.append(right)
            right = right + 1

        result = []
        for key in range(length):
            result.append(mapping.get(key, 0))
        return result


if __name__ == "__main__":
    s = Solution()
    r = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(r)
    assert r == [1, 1, 4, 2, 1, 1, 0, 0]

    r = s.dailyTemperatures([73])
    print(r)
    assert r == [0]
