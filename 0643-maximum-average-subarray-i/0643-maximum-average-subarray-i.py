class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curr_arr = nums[:k]
        curr_avg = sum(nums[:k])/k
        res = [curr_avg]
        j = 1

        for i in range(1,len(nums)-k+1):
            curr_avg -= nums[i-1]/k
            curr_arr = nums[i:k+j]
            j += 1
            curr_avg += curr_arr[-1]/k
            # curr_avg /= k
            res.append(curr_avg)

        return max(res)


# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:

#         curr_arr = nums[:k]
#         curr_avg = sum(nums[:k])/k
#         res = [curr_avg]

#         for i in range(1,len(nums)-k+1):
#             curr_avg -= nums[i-1]/k
#             curr_arr = nums[i:k+i]
#             curr_avg += curr_arr[-1]/k
#             # curr_avg /= k
#             res.append(curr_avg)

#         return max(res)


# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
        
#         curr_avg = sum(nums[:k])/k
#         res = curr_avg

#         for i in range(1,len(nums)-k+1):
#             curr_avg -= nums[i-1]/k                
#             curr_avg += nums[i+k-1]/k
#             # We are doing -1 here every time because, indecies 
#             # start from 0 always
#             # curr_avg /= k
#             res = max(res,curr_avg)

#         return res