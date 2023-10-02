class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:

        l = []
        res = ""

        for i in s:
            l.append(i)

        for i in range(len(l)):
            if(l[i] == l[len(l)-i-1]):
                continue
            else:
                if(ord(l[len(l)-i-1]) < ord(l[i])):
                    l[i] = l[len(l)-i-1]
                else:
                    l[len(l)-i-1] = l[i]

        for i in l:
            res += i
        
        return res