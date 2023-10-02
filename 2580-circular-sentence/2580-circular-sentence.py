class Solution:
    def isCircularSentence(self, s: str) -> bool:

        l = s.split(" ")
        res = 0

        if(l[0][0] == l[len(l)-1][-1]):
            for i in range(len(l)):
                if(i != len(l)-1):
                    if(l[i][-1] == l[i+1][0]):
                        res = 1
                    else:
                        res = 2
                        break

            if(len(l) == 1 and l[0][0] == l[0][-1]):
                res = 1

        if(res == 1):
            return True
        else:
            return False