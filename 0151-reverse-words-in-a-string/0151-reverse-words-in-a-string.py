class Solution:
    def reverseWords(self, s: str) -> str:
        
        t = ""
        l = s.split(" ")
        l.reverse()
        r = False

        for i in range(len(l)):
            if(l[i].isalnum()):
                t += l[i]
                for j in range(len(l[i+1:])):   
                    if((l[i+1:][j].isalnum())): # Even if there is a single alphanumeric word after l[i], then we set r to True and if r is True we will add space after l[i]
                        r = True
                        break
                if(r):
                    t += " "
# But when we do this, we will be having a space at last too
# To remove it,
        l_ = t.split(" ")
        t_ = ""

        for i in range(len(l_)):
            if(l_[i] != ""):
                t_ += l_[i]
            if(i != len(l_)-1 and i != len(l_)-2):
                t_ += " "
                
        return t_