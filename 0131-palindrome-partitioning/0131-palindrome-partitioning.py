class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []    # Partitions

        def rec(ind):

            if ind > len(s) - 1:
                res.append(part.copy())
                return
            
            for i in range(ind , len(s)):
                if s[ind : i + 1] == s[ind : i + 1][::-1]:
                    part.append(s[ind : i + 1])
                    rec(i + 1)
                    part.pop()

        rec(0)

        return res