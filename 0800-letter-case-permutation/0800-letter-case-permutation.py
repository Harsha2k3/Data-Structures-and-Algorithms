class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        res = []

        def rec(ind , l):

            nonlocal res

            if ind == len(l):
                res.append("".join(l))
                return

            if l[ind].isdigit():
                rec(ind + 1 , l)

            if l[ind].isalpha():
                rec(ind + 1 , l)

                if l[ind].isupper(): l[ind] = l[ind].lower()
                else: l[ind] = l[ind].upper()
                rec(ind + 1 , l)
                if l[ind].isupper(): l[ind] = l[ind].lower()
                else: l[ind] = l[ind].upper()
        
        rec(0 , list(s))

        return res