class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, t: int) -> int:

        curr_arr = nums[:k]
        curr_avg = sum(nums[:k])/k
        count = 0
        if(curr_avg >= t):
            count += 1
        j = 1

        for i in range(1,len(nums)-k+1):
            curr_avg -= nums[i-1]/k
            curr_arr = nums[i:k+j]
            j += 1
            curr_avg += curr_arr[-1]/k
            if(curr_avg >= t):
                count += 1

        return count