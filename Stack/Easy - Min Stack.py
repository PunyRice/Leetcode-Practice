class MinStack:
    # one stack solution
    def __init__(self):
        self.items = []
        self.minimum = float("inf")

    def push(self, val: int) -> None:
        self.minimum = min(self.minimum, val)
        self.items.append(val)

    def pop(self) -> None:
        self.items.pop()
        self.minimum = min(self.items, default=float("inf"))

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minimum

class MinStack:
    # two stack solution
    def __init__(self):
        self.items = []  # this is our actual stack
        self.minimum = []  # this keeps track of minimum values at each index of items

    def push(self, val: int) -> None:
        self.items.append(val)
        # statement (runs when true) if condition else statement (runs when false)
        num = min(val, self.minimum[-1] if self.minimum else val)
        self.minimum.append(num)


    def pop(self) -> None:
        self.minimum.pop()
        self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minimum[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()