import math as m


class Solution:

    def get_sum(self, k, nums):

        sum = 0

        for i in nums:
            sum += m.ceil(i / k)

        return sum

    def smallestDivisor(self, nums: List[int], t: int) -> int:

        left = 1
        right = max(nums)

        res = float("inf")

        while left <= right:

            mid = (left + right) // 2

            if self.get_sum(mid, nums) > t:
                left = mid + 1

            else:
                res = min(res, mid)
                right = mid - 1

        return res
