class Solution:
    def doesAliceWin(self, s: str) -> bool:

        pc = [0] * (len(s) + 1)

        for i in range(len(s)):
            pc[i + 1] = pc[i] + (1 if s[i] in "aeiou" else 0)

        odd_count = 0
        even_count = 0
        
        for count in pc:
            
            if count % 2 == 0:
                even_count += 1
                
            else:
                odd_count += 1
                
        if even_count == 0:
            return True        # Alice
        
        if odd_count == 0:
            return False

        return True