class Solution(object):
    def minSwaps(self, nums):

        start = 0
        zc = 0    # Zero count

        res = float("inf")   # Min 0's in a sub array of size k

        k = nums.count(1)

        nums = nums + nums

        for end in range(len(nums)):
            if nums[end] == 0:
                zc += 1
            
            if end - start + 1 == k:
                res = min(res , zc)
                
                if nums[start] == 0:
                    zc -= 1
                
                start += 1

        return res if res != float("inf") else 0