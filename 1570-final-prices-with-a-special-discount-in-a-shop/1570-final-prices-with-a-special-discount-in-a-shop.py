class Solution:
    def finalPrices(self, nums: List[int]) -> List[int]:

        nums_ = nums.copy()
        res = []
        stack = []
        k = 0

        for i in range(len(nums)):
            k = nums[len(nums)-i-1]   
            # Storing it in a temporary variable
            
            if(stack and stack[-1] <= nums[len(nums)-i-1]):
                nums[len(nums)-i-1] -= stack[-1]
                
            elif(stack and stack[-1] > nums[len(nums)-i-1]):
                while(stack and stack[-1] > nums[len(nums)-i-1]):
                    stack.pop()
                if(stack):
                    nums[len(nums)-i-1] -= stack[-1]
                    
            stack.append(k)
            
        # for i in range(len(nums)):
        #     res.append(nums_[i]-nums[i])

        # return res
        return nums