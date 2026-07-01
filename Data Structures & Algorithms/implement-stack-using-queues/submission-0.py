class MyStack:

    def __init__(self):
        self.hm = []

    def push(self, x: int) -> None:
        self.hm.append(x)

    def pop(self) -> int:
        val = self.top()
        del self.hm[-1]
        return val

    def top(self) -> int:
        return self.hm[-1]

    def empty(self) -> bool:
        return len(self.hm) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()