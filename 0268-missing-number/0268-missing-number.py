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