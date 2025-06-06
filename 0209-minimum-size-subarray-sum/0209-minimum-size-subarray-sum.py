# Dynamic Sized Sliding Window (Length of Sub-array is not given)

class Solution:
    def minSubArrayLen(self, t: int, nums: List[int]) -> int:

        # start = 0
        # end = 0
        # curr_sum = nums[start]

        # min_length = float("inf")

        # while(end < len(nums)):
        #     if(curr_sum >= t):
        #         min_length = min(min_length, end - start + 1)
        #         curr_sum -= nums[start]
        #         start += 1
        #     else:
        #         end += 1
        #         if end < len(nums):
        #             curr_sum += nums[end]

        # if(min_length == float("inf")):
        #     return 0
        # return min_length


        start = 0
        curr_sum = 0

        ml = float("inf")   # Min-length

        for end in range(len(nums)):
            curr_sum += nums[end]

            while curr_sum >= t:
                ml = min(ml , end - start + 1)
                curr_sum -= nums[start]
                start += 1
        
        if ml == float("inf"):
            return 0
        return ml