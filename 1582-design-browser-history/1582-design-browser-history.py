class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.temp = ListNode(homepage)


    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        new_node.prev = self.temp
        self.temp.next = new_node
        self.temp = new_node


    def back(self, steps: int) -> str:
        while(steps and self.temp.prev):
            self.temp = self.temp.prev
            steps -= 1

        return self.temp.val

        

    def forward(self, steps: int) -> str:
        while(steps and self.temp.next):
            self.temp = self.temp.next
            steps -= 1

        return self.temp.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)