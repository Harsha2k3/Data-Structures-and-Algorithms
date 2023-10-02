class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if(len(s.split(" ")[-1]) != 0):
            return len(s.split(" ")[-1])
        
        else:
            l = s.split(" ")
            l.reverse()

            for i in range(len(l)):
                if(len(l[i]) == 0):
                    continue
                else:
                    return len(l[i])
                    break