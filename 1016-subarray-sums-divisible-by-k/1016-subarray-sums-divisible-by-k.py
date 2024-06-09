class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        map = {0 : [-1]}  # To handle the case where the sub-array starts from index 0
        ps = 0
        count = 0

        for i in range(len(nums)):
            ps += nums[i]
            rem = ps % k

            if rem in map:
                map[rem].append(i)
                count += len(map[rem]) - 1
            else:
                map[rem] = [i]

        return count