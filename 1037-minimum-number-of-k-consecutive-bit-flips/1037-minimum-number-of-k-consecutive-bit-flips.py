class Solution(object):
    def minKBitFlips(self, nums, k):
        
        flipped = 0
        res = 0
        isFlipped = [0] * len(nums)
        
        for i in range(len(nums)):

            if i >= k:
                flipped ^= isFlipped[i - k]

            if flipped == nums[i]:
                if i + k > len(nums):
                    return -1

                isFlipped[i] = 1
                flipped ^= 1
                res += 1
        
        return res