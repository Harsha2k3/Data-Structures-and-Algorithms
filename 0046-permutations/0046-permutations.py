class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def rec(ind , nums):

            if ind > len(nums) - 1:
                res.append(nums.copy())
                return

            for i in range(ind , len(nums)):
                nums[ind] , nums[i] = nums[i] , nums[ind]
                rec(ind + 1 , nums)
                nums[ind] , nums[i] = nums[i] , nums[ind]
        
        rec(0 , nums)

        return res

















        
        # res = []

        # def rec(nums , l , h):

        #     if len(l) == len(nums):
        #         res.append(l.copy())
        #         return
            
        #     for i in range(len(nums)):
        #         if not h[i]:
        #             l.append(nums[i])
        #             h[i] = 1
        #             rec(nums , l , h)
        #             l.pop()
        #             h[i] = 0
        
        # rec(nums , [] , [0] * len(nums))

        # return res