class Solution:
    def minAddToMakeValid(self, S):
        stack = []
        for char in S:
            if char == '(':
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    stack.append(char)

        return len(stack)
