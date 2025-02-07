from collections import defaultdict 

class Solution:
    def queryResults(self, limit: int, q: List[List[int]]) -> List[int]:
        
        count = 0
        res = []
        s = set()

        colors = defaultdict(int)  
        color_count = defaultdict(int)  

        for i in q:
            temp = colors.get(i[0] , -1)
            colors[i[0]] = i[1]
            if temp != -1:
                color_count[temp] -= 1  
                if color_count[temp] == 0:
                    s.remove(temp)  

            color_count[i[1]] += 1  
            
            if i[1] not in s:
                s.add(i[1])
            
            res.append(len(s))

        return res