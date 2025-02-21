class CustomStack:
    def __init__(self, maxSize: int):
        self.custom_stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.custom_stack) == self.max_size:
            return
        self.custom_stack.append(x)

    def pop(self) -> int:
        if len(self.custom_stack) == 0:
            return -1
        return self.custom_stack.pop()

    def increment(self, k: int, val: int) -> None:
        if k > len(self.custom_stack):
            k = len(self.custom_stack)
        for i in range(k):
            self.custom_stack[i] = self.custom_stack[i] + val


args1 = [
    "CustomStack",
    "push",
    "push",
    "pop",
    "push",
    "push",
    "push",
    "increment",
    "increment",
    "pop",
    "pop",
    "pop",
    "pop",
]
args2 = [[3], [1], [2], [], [2], [3], [4], [5, 100], [2, 100], [], [], [], []]

for arg1, arg2 in zip(args1, args2):
    if arg1 == "CustomStack":
        cs = CustomStack(maxSize=arg2)
    elif arg1 == "push":
        print(cs.push(arg2[0]))
    elif arg1 == "pop":
        print(cs.pop())
    elif arg1 == "increment":
        print(cs.increment(arg2[0], arg2[1]))


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
