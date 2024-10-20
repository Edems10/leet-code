from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = deque(maxlen=k)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        if len(self.deque) > 0:
            return False
        return True

    def isFull(self) -> bool:
        if self.deque.maxlen == len(self.deque):
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
param_1 = print(obj.insertLast(1))
param_2 = print(obj.insertLast(2))
param_3 = print(obj.insertFront(3))
param_4 = print(obj.insertFront(4))
param_5 = print(obj.getRear())
param_6 = print(obj.isFull())
param_7 = print(obj.deleteLast())
param_8 = print(obj.insertFront(4))
param_9 = print(obj.getFront())
