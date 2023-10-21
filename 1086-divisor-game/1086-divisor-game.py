class Solution:
    def divisorGame(self, n: int) -> bool:
        
        # Find if n is even or idd

        if(n & 1 == 0):
            return True
        else:
            return False