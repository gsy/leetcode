#!/usr/bin/env python3

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = None


    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minimum is None or x < self.minimum:
            self.minimum = x

    def pop(self) -> None:
        x = self.stack.pop(-1)
        if len(self.stack) == 0 or x == self.minimum:
            self.minimum = None
            for item in self.stack:
                if self.minimum is None or item < self.minimum:
                    self.minimum = item

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
print(obj.stack)
obj.pop()
print(obj.stack)
r = obj.top()
print(r)

obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.stack)
r = obj.getMin()
print(r)
obj.pop()

r = obj.top()
print(r)
r = obj.getMin()
print(r)
