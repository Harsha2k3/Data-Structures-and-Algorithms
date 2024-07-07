class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        res = []
        
        def valid(s):
            
            for i in range(len(s) - 1):
                if s[i] == "0" and s[i + 1] == "0":
                    return False
            return True
        
        def rec(n , s , res):
            
            if len(s) == n:
                if valid(s):
                    res.append(s)
                return
            
            rec(n , s + "0" , res)
            rec(n , s + "1" , res)
            
        rec(n , "" , res)
        
        return res