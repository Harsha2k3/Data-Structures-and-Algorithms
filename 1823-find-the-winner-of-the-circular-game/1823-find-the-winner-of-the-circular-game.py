class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        l = [i for i in range(1,n+1)]
        
        # j = -1

        def rec(j,l):

            if(len(l) == 1):
                return l[0]

            else:
                j += k
                j %= len(l)
                l.pop(j)
                return rec(j-1,l)

        return rec(-1,l)