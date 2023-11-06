class Solution:
    def findComplement(self, num: int) -> int:
        
        return num^(2**(len(bin(num)[2:]))-1)

        # Just do XOR with all 1's
        # Because, if we have 0 ==> 0 XOR 1 = 1 (0 -> 1) 
        # If we have 1 ==> 1 XOR 1 = 0 (1 -> 0)
        # For doing that, just do 2 ** (Length of the given binary number)
        # Just take case where, num = 5
        # Now, 5 ==> 101
        # So,  2 ** 3 = 8
        # But, 8 ==> 1000
        # So,  As we know that of a number is in powers of 2 then the number before it contains sum all the powers of 2 before that number
        # So, 8 - 1 = 7 and 7 ==> 111
        # So, we have to do 2**(len(bin(num)[2:]))-1