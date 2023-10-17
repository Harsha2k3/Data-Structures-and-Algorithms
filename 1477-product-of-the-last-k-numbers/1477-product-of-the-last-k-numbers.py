class ProductOfNumbers:

    def __init__(self):
        self.p = []
        self.prod = 1

    def add(self, num: int) -> None:
        if(num != 0):
            self.prod *= num
            self.p.append(self.prod)
        else:
            self.p = []
            self.prod = 1
        

    def getProduct(self, k: int) -> int:
        if(len(self.p) == k):
            return self.p[-1]
        elif(len(self.p) < k):
            return 0
        else:
            if(self.p[-k-1] != 0):
                return int(self.p[-1] / self.p[-k-1])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)