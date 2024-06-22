class Solution(object):
    def letterCasePermutation(self, s):
        
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
                l[ind] = l[ind].upper() if l[ind].islower() else l[ind].lower()
                rec(ind + 1, l)
                
                # Backtrack
                l[ind] = l[ind].upper() if l[ind].islower() else l[ind].lower()

        rec(0, list(s))

        return res