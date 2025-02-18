class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        count, ans, n = collections.Counter(), 0, len(nums)

        for i in range(n):
            for j in range(i+1, n):
                ans += 8 * count[nums[i]*nums[j]]
                count[nums[i]*nums[j]] += 1
                
        return ans