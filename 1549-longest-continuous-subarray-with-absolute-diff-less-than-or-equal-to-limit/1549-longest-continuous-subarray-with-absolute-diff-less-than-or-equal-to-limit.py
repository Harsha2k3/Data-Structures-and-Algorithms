class Solution(object):
    def longestSubarray(self, nums, limit):

        maxLength = 0

        minQueue = deque()
        maxQueue = deque()
        
        
        start , end = 0 , 0
        n = len(nums)
        
        while end < n:
            # We only want bigger elements in maxQueue
            while len(maxQueue) > 0 and maxQueue[-1] < nums[end]: maxQueue.pop()
            maxQueue.append(nums[end])
            
            # We only want smaller elements in minQueue
            while len(minQueue) > 0 and minQueue[-1] > nums[end]: minQueue.pop()
            minQueue.append(nums[end])
            
            # Make sure the maximum absolute difference is <= limit
            while len(maxQueue) > 0 and len(minQueue) > 0 and maxQueue[0] - minQueue[0] > limit:
                if maxQueue[0] == nums[start]: maxQueue.popleft()
                if minQueue[0] == nums[start]: minQueue.popleft()
                start += 1
                
            # Update the maxLength if current window length is bigger than previous maxLength
            maxLength = max(maxLength, end - start + 1)
            end += 1
        
        return maxLength