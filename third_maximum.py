# -*- coding: utf-8 -*-


class Solution:
    def thirdMax(self, nums):
        stack = []
        remain = []
        for num in nums:
            if len(stack) == 0:
                stack.append(num)
            else:
                while len(stack) > 0:
                    top = stack[-1]
                    if top < num:
                        remain.append(stack.pop(-1))
                    elif top == num:
                        stack.pop(-1)
                    else:
                        break

                if len(stack) < 3:
                    stack.append(num)

                while len(stack) < 3 and len(remain) > 0:
                    stack.append(remain.pop(-1))

        return stack[-1] if len(stack) == 3 else stack[0]


if __name__ == '__main__':
    s = Solution()
    r = s.thirdMax([1, 2])
    print(r)
    assert r == 2

    r = s.thirdMax([3, 1, 2])
    print(r)
    assert r == 1

    r = s.thirdMax([3, 1, 2, 2])
    print(r)
    assert r == 1

    r = s.thirdMax([1, 2, 2, 3])
    print(r)
    assert r == 1

    r = s.thirdMax([1, 2, 2, 2, 3])
    print(r)
    assert r == 1

    r = s.thirdMax([2, 2, 2, 2, 3])
    print(r)
    assert r == 3
