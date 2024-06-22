class Solution(object):
    def letterCasePermutation(self, s):

        # Take or not take pattern (Like in )

        res = []

        def rec(ind, l):
            if ind == len(s):
                res.append("".join(l))
                return

            if l[ind].isdigit():
                rec(ind + 1, l)

            else:
                # Recur without changing the case
                rec(ind + 1, l)

                # Recur after changing the case
                if l[ind].islower():
                    l[ind] = l[ind].upper()  
                else:
                    l[ind] = l[ind].lower()
                    
                rec(ind + 1, l)
                
                # Backtrack
                if l[ind].islower():
                    l[ind] = l[ind].upper()  

                else:
                    l[ind] = l[ind].lower()

        rec(0, list(s))

        return res