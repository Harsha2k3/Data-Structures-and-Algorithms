class Solution:
    def numSteps(self, s: str) -> int:
        
        steps = 0

        n = int("0b" + s , 2)

        while(n != 1):
            if(n % 2 == 0):
                n //= 2
            else:
                n += 1
            steps += 1
        
        return steps