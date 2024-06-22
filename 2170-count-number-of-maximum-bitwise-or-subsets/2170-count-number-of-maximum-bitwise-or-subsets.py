class Solution(object):
    def countMaxOrSubsets(self, nums):

        br = nums[0]

        for i in range(1 , len(nums)):
            br |= nums[i]    

        def rec(i , cr , count):    # Current or

            if i == len(nums):
                if cr == br: 
                    return 1
                return 0

            count += rec(i + 1 , cr | nums[i] , count) + rec(i + 1 , cr , count)

            return count

        return rec(0 , 0 , 0)