class Solution:
    def splitWordsBySeparator(self, w: List[str], s: str) -> List[str]:

        l = []
        l_ = []

        for i in w:
            for j in i.split(s):
                l.append(j)
        
        for i in l:
            if(i != ""):
                l_.append(i)
            else:
                continue

        return l_