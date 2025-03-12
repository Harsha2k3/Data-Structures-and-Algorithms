class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        # 2 ptr's

        l = 0
        r = 0

        while r < len(nums):
            if nums[r]:
                nums[l] , nums[r] = nums[r] , nums[l]
                l += 1
            r += 1
        
        return nums

        # [0,1,0,3,12]
        # [1,0,0,3,12]
        # [1,0,0,3,12]
        # [1,3,0,0,12]
        # [1,3,12,0,0]