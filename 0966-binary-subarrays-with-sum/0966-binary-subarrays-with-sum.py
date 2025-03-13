class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # Returns no.of sub-arrays whose sum <= k

        def helper(k):

            if k < 0:
                return 0
            
            start = 0
            curr_sum = 0
            res = 0

            for end in range(len(nums)):
                curr_sum += nums[end]

                while curr_sum > k:
                    curr_sum -= nums[start]
                    start += 1
                
                res += (end - start + 1)
            
            return res
        
        return helper(goal) - helper(goal - 1)


        # def helper(k):

        #     if(k < 0):
        #         return 0

        #     curr_sum = 0
        #     res = 0
        #     l = 0

        #     for r in range(len(nums)):
        #         curr_sum += nums[r]

        #         while(curr_sum > k):
        #             curr_sum -= nums[l]
        #             l += 1

        #         res += (r - l + 1)

        #     return res

        # return helper(goal) - helper(goal - 1)


        # Here, 1 ==> sum = 1 <= 2 ==> res = 1
        # 2 ==> sum = 1 <= 2 ==> res = 1 + 2 = 3
        # 3 ==> sum = 2 <= 2 ==> res = 3 + 3 = 6
        # 4 ==> sum = 2 <= 2 ==> res = 6 + 4 = 10
        # 5 ==> sum = 3 > 2

        # Now, in each of these iterations we add the size because,
        # Say we are at index 2 (2nd iteration),
        # window = 1 0
        # No.of possible sub-arrays with sum <= goal are 1 , 0 and 1 0
        # i.e, 3 (1 + 2 = 3)
        
        # Say we are at index 3 (3rd iteration),
        # window = 1 0 1
        # No.of possible sub-arrays with sum <= goal are 1 , 0 , 1 , 1 0 , 0 1 , 1 0 1 
        # i.e, 3 (1 + 2 + 3 = 6)