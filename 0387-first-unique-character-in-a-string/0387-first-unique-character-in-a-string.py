class Solution:
    def firstUniqChar(self, s: str) -> int:

        l = [i for i in s]
        q = []              # Queue
        l_ = []

        for i in l:
            if(i not in q and i not in l_):
                q.append(i)
            elif(i in l_):
                continue
            else:
                l_.append(i)
                q.remove(i)

        if(q == []):
            return -1
        return l.index(q[0])