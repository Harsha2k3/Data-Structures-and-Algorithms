class Solution:
    def kidsWithCandies(self, c: List[int], e: int) -> List[bool]:
        
        l = []

        for i in range(len(c)):
            if(c[i]+e >= max(c)):
                l.append(True)
            else:
                l.append(False)
                
        return l