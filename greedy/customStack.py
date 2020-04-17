class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.capacity = 0

    def push(self, x: int) -> None:
        if self.capacity < self.maxSize:
            self.stack.append(x)
            self.capacity += 1

    def pop(self) -> int:
        if self.capacity == 0:
            return -1
        else:
            self.capacity -= 1
            return self.stack.pop(-1)

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.capacity)):
            self.stack[i] = self.stack[i] + val


if __name__ == '__main__':
    obj = CustomStack(3)
    obj.push(1)
    obj.push(2)
    print(obj.pop())
    obj.push(2)
    obj.push(3)
    obj.push(4)
    print(obj.stack)
    obj.increment(5, 100)
    print(obj.stack)
    obj.increment(2, 100)
    print(obj.stack)
    obj.pop()
    print(obj.stack)
    obj.pop()
    print(obj.stack)
    print(obj.pop())
    print(obj.stack)
    print(obj.pop())
    print(obj.stack)
