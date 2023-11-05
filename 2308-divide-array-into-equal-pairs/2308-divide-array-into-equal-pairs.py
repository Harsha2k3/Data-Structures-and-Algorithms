class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        n = len(nums) / 2

        nums.sort()

        xor = 0
        count = 0

        for i in nums:
            xor ^= i
            if(xor != 0):
                count += 1

        return count == n