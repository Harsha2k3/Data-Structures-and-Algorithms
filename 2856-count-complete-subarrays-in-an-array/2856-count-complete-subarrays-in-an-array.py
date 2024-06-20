class Solution:
    def countCompleteSubarrays(self, nums):

        k = len(set(nums))
        return self.subarraysWithAtMostKDistinct(nums, k) - self.subarraysWithAtMostKDistinct(nums, k - 1)

    def subarraysWithAtMostKDistinct(self, nums, k):
        ans = 0
        count = [0] * 2001

        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            if count[nums[r]] == 1:
                k -= 1
            while k == -1:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    k += 1
                l += 1
            ans += r - l + 1
        return ans