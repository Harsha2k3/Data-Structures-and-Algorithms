class Solution:
    def clearDigits(self, s: str) -> str:
        
        l = []
        ind = []
        rind = []

        for i in range(len(s)):
            
            if s[i].isalpha():
                ind.append(i)
            
            else:
                rind.append(ind.pop())
                rind.append(i)

        s = list(s)
        
        return "".join([num for i , num in enumerate(s) if i not in set(rind)])