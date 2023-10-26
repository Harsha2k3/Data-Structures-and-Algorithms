import math as m

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        res = []

        for i in range(1,int(m.sqrt(n))+1):
            if(n%i == 0):
                if(n/i == i):
                    res.append(i)
                else:
                    res.append(i)
                    res.append(int(n/i))

        res.sort()

        return res[k-1] if len(res) >= k else -1