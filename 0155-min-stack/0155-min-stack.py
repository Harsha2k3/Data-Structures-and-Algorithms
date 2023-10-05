# class MinStack:

#     def __init__(self):
#         self.list = []

#     def push(self, val: int) -> None:
#         self.list.append(val)

#     def pop(self) -> None:
#         self.list.pop()

#     def top(self) -> int:
#         return self.list[len(self.list)-1]

#     def getMin(self) -> int:
#         return min(self.list)   ==> This will take O(n)



# But we need to do it in constant time (O(1))


class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(self.minstack):
            self.minstack.append(min(val,self.minstack[-1]))
        else:
            self.minstack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()