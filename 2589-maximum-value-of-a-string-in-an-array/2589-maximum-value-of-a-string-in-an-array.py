class Solution:
    def maximumValue(self, s: List[str]) -> int:

        k,l,m = 0,0,0

        for i in range(len(s)):

            if(s[i].isnumeric()):
                m = max(m,int(s[i]))

            elif(s[i].isalpha()):
                l = max(l, len(s[i]))

            elif(s[i].isalnum()):
                k = max(k,len(s[i]))
            
        return max(k,l,m)