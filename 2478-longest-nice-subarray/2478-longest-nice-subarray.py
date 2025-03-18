class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        max_length = 0
        left = 0
        window_and = 0  

        for right in range(len(nums)):

            while (window_and & nums[right]) != 0:  
                window_and ^= nums[left]  
                left += 1

            window_and |= nums[right]  
            max_length = max(max_length, right - left + 1)

        return max_length