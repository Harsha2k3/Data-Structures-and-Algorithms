class CombinationIterator(object):

    def __init__(self, char, combinationLength):

        self.res = []

        def rec(ind , l):

            if len(l) == combinationLength:
                self.res.append("".join(l))
                return
            
            for i in range(ind , len(char)):
                l.append(char[i])
                rec(i + 1 , l)
                l.pop()
            
        rec(0 , [])


    def next(self):
        return self.res.pop(0)
        

    def hasNext(self):
        if self.res:
            return True
        return False