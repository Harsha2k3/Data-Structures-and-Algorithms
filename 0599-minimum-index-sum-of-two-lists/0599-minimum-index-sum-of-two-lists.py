class Solution:
    def findRestaurant(self, l1: List[str], l2: List[str]) -> List[str]:

        l = []
        ind = []
        res = []

        for i in range(len(l1)):
            for j in range(len(l2)):
                if(l1[i] == l2[j]):
                    l.append(l1[i])
                    ind.append(i+j)

        for i in range(len(ind)):
            if(ind[i] == min(ind)):
                res.append(l[i])
        
        return res