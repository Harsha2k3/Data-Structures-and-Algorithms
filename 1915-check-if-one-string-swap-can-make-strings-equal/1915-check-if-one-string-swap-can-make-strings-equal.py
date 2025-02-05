class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        nep = 0
        s = ""
        s_ = ""

        for i in range(len(s1)):

            if s1[i] != s2[i]:
                nep += 1

                if nep == 1:
                    s += s1[i]
                    s += s2[i]
                
                if nep == 2:
                    s_ += s2[i]
                    s_ += s1[i]
        
        return (nep == 2 or nep == 0) and (s == s_)