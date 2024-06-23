class Solution(object):
    def minimumAverage(self, nums):
        
        nums.sort()
        
        avgs = []
        
        while nums:
            
            avgs.append(float(nums.pop(0) + nums.pop(-1)) / 2)
            
        return round(min(avgs) , 1)