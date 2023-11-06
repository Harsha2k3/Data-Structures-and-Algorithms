class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # For knowing if a number is in powers of 2, we just do n & (n-1) == 0
        # But, for knowing if a number is in powers of 4, we do n & (n-1) == 0 and (n-1) % 3 == 0
        # Because, 4  ==> 3 (Divisible by 3)
                #  16 ==> 15 (Divisible by 3)
                #  64 ==> 63 (Divisible by 3)
                #  256 ==> 255 (Divisible by 3)

        if((n & (n-1) == 0) and ((n-1) % 3 == 0)):
            return True
        return False