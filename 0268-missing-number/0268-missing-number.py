class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        l = []

        for i in range(len(nums) + 1):
            l.append(i)

        l_ = l + nums

        xor = 0

        for i in l_:
            xor = xor ^ i
        
        return xor

        # Just apply XOR between the given array and array that has the numbers from 0 to n (inclusive)