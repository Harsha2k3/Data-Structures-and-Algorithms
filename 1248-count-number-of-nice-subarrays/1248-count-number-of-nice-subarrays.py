class Solution:
    def numberOfSubarrays(self, nums: List[int], goal: int) -> int:

        # No. of subarrays with exactly k odd = No. of subarrays with at most k odd - No. of subarrays with at most k-1 odd

        # Returns no.of sub-arrays whose odds <= k

        def helper(k):

            odds = 0
            res = 0
            l = 0

            for r in range(len(nums)):
                if nums[r] % 2 != 0:
                    odds += 1 

                while(odds > k):
                    if nums[l] % 2 != 0:
                        odds -= 1 
                    l += 1

                res += (r - l + 1)

            return res

        return helper(goal) - helper(goal - 1)

        # We might expect this code will work, but it'll not
        # So follow above method

        # odds = 0
        # count = 0
        # start = 0

        # for end in range(len(nums)):
        #     if nums[end] % 2 != 0:
        #         odds += 1
            
        #     while(odds > k):
        #         if nums[start] % 2 != 0:
        #             odds -= 1
        #         start += 1
            
        #     if odds == k:
        #         count += 1
        
        # return count