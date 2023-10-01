class Solution:
    def haveConflict(self, e1: List[str], e2: List[str]) -> bool:

        res = False

        if(e1[1] >= e2[0] and e1[0] <= e2[1]):
            res = True

        if(res == True):
            return res
        else:
            return res