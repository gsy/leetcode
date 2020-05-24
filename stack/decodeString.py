#!/usr/bin/env python3

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                encoded = ""
                while len(stack) > 0:
                    tmp = stack.pop(-1)
                    if tmp == '[':
                        break
                    encoded = tmp + encoded
                digit = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    digit = stack.pop(-1) + digit
                k = int(digit)
                stack.append(encoded * k)
            else:
                stack.append(char)

        result = ""
        while len(stack) > 0:
            result = stack.pop() + result
        return result

if __name__ == '__main__':
    s = Solution()
    r = s.decodeString("3[a]2[bc]")
    print(r)
    r = s.decodeString("3[a2[c]]")
    print(r)
    r = s.decodeString("2[abc]3[cd]ef")
    print(r)
    r = s.decodeString("12[abc]3[cd]ef")
    print(r)

    r = s.decodeString("100[leetcode]")
    print(r)
