import math as m

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        res_a = []
        res_b = []

        for i in range(1,int(m.sqrt(a))+1):
            if(a%i == 0):
                if(a/i == i):
                    res_a.append(i)
                else:
                    res_a.append(i)
                    res_a.append(int(a/i))

        res_a.sort()

        for i in range(1,int(m.sqrt(b))+1):
            if(b%i == 0):
                if(b/i == i):
                    res_b.append(i)
                else:
                    res_b.append(i)
                    res_b.append(int(b/i))

        res_b.sort()

        count = 0

        for i in res_a:
            if(i in res_b):
                count += 1

        return count