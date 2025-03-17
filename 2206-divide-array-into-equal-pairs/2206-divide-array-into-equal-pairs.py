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

        # Just sort them
        # Now, xor all the integers in nums
        # xor will be not be 0, when the pair ends and new pair starts
        # Just simply count the cases where xor is not 0