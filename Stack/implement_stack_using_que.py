from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def rotate(self, n: int):
        i = 0
        while i < n:
            l = self.q.popleft()
            self.q.append(l)
            i += 1

    def push(self, x: int) -> None:
        self.q.append(x)
        self.rotate(len(self.q) - 1)

    def pop(self) -> int:
        x = self.q.popleft()
        return x

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not bool(self.q)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()