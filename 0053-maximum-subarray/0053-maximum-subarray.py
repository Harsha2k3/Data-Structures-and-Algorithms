class Solution:
    def maxSubArray(self, l: List[int]) -> int:

        max_sum_ending_here = 0   
        # Maximum sum ending at current element
        
        res = float("-inf")

        for i in l:
            max_sum_ending_here += i
            
            if(max_sum_ending_here > res):
                res = max_sum_ending_here
                
            if(max_sum_ending_here < 0):    
                max_sum_ending_here = 0

        return res