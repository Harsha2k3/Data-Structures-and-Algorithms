class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def rec(s , open_ , close):

            if len(s) == 2 * n:
                res.append(s)
                return
            
            if open_ < n:
                rec(s + "(" , open_ + 1 , close)

            if close < open_:
                rec(s + ")" , open_ , close + 1)
        
        rec("" , 0 , 0)

        return res