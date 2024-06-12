class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # Bubble sort
        
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if(nums[j+1] < nums[j]):
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]

        return nums