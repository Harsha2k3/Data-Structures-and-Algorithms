class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        
        elif len(nums) == 2:
            if (nums[0] % 2 == 0 and nums[1] % 2 != 0) or (nums[0] % 2 != 0 and nums[1] % 2 == 0):
                return True
            else:
                return False

        res = True

        for i in range(1 , len(nums) - 1):
            
            if (nums[i] % 2 == 0 and nums[i - 1] % 2 != 0 and nums[i + 1] % 2 != 0) or (nums[i] % 2 != 0 and nums[i - 1] % 2 == 0 and nums[i + 1] % 2 == 0):
                res = True
            
            else:
                return False

        return True