class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        res = True 

        for i in range(len(nums)):
            if i != 0:
                if nums[i] % 2 == 0:
                    res = res and (nums[i - 1] % 2 == 1)
                else:
                    res = res and (nums[i - 1] % 2 == 0)
                
                if res == False:
                    break 
        
        return res