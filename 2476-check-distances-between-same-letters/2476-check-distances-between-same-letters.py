class Solution:
    def checkDistances(self, s: str, d: List[int]) -> bool:

        lm = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        l_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

        
        li = []
        count = 0
        li_ = []
        l,k = 0,0

        for i in s:
            if(i not in li):
                li.append(i)
        
        for i in li:
            for j in range(len(s)):
                if(s[j] == i):
                    if(count == 0):
                        count += 1
                        k = j
                    elif(count == 1):
                        l = j
                        count = 0
                        m = (l-k)-1
                        li_.append(m)
        
        res = 0

        for i in range(len(li)):
            for j in range(len(lm)):
                if(li[i] == lm[j]):
                    h = j
                    break
            if(li_[i] == d[h]):
                res = 1
            else:
                res = 2
                break
        
        if(res == 1):
            return True
        else:
            return False