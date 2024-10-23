class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        # Take or not take pattern (Like in )

        res = []

        def rec(ind , l):

            if ind == len(s):
                res.append("".join(l))
                return

            if l[ind].isdigit():
                rec(ind + 1, l)

            else:

                rec(ind + 1 , l)
                
                if l[ind].islower():
                    l[ind] = l[ind].upper()
                    rec(ind + 1 , l)

                else:
                    l[ind] = l[ind].lower()
                    rec(ind + 1 , l)
                
                if l[ind].islower():
                    l[ind] = l[ind].upper()

                else:
                    l[ind] = l[ind].lower()
        
        rec(0 , list(s))

        return res