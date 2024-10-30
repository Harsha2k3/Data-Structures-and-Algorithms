class Solution:
    def maximumEvenSplit(self, fs: int) -> List[int]:

        res = []
        
        if fs % 2:
            return []

        # npn ==> Next possible number
        
        def rec(npn , l , rem):

            nonlocal res

            if rem <= 0:
                if len(res) < len(l):
                    res = l[:]
                    return True
                return

            for i in range(npn , fs + 2 , 2):

                if rem - i < 0:
                    break

                l.append(i)
                if rec(npn + 2 , l , rem - i):
                    return True
                l.pop()
        
        rec(2 , [] , fs)

        return res