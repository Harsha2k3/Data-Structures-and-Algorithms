class Solution:
    def maxLength(self, arr: List[str]) -> int:

        res = 0

        def rec(ind , l):
            
            nonlocal res
            
            if len("".join(l)) == len("".join(arr)):
                return

            for i in range(ind , len(arr)):
                
                l.append(arr[i])

                if len("".join(l)) == len(set("".join(l))):
                    res = max(res , len("".join(l)))
                    rec(i + 1 , l)
                
                l.pop()
        
        rec(0 , [])

        return res