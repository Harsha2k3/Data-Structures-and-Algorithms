class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = 1
        s = s.lower()
        l = []
        l_ = []

        for i in s:
            l.append(i)
        
        for i in l:
            if(i.isalnum()):
                l_.append(i)
        
        for i in range(len(l_)):
            if(l_[i] != l_[len(l_)-i-1]):
                res = 0

        if(res == 1):
            return True
            
        else:
            return False