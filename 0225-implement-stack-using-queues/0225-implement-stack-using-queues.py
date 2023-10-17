from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if not self.queue1:
            return -1  

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        item = self.queue1.popleft()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return item

    def top(self) -> int:
        if not self.queue1:
            return -1  

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        item = self.queue1.popleft()
        self.queue2.append(item)

        self.queue1, self.queue2 = self.queue2, self.queue1

        return item

    def empty(self) -> bool:
        return not self.queue1