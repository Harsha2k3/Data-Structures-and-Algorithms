class Solution(object):
    def minOperations(self, nums):

        ops = 0
        
        for i in range(len(nums)-2):

            if nums[i] == 0:

                nums[i] = 1

                if nums[i+1] == 0:
                    nums[i+1] = 1
                else:
                    nums[i+1] = 0

                if nums[i+2] == 0:
                    nums[i+2] = 1
                else:
                    nums[i+2] = 0

                ops += 1
        
        if nums[-1] == nums[-2] == nums[-3] == 1: 
            return ops

        return -1