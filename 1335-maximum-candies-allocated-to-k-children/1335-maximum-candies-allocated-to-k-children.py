class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        if sum(candies) < k:
            return 0
        
        left = 1
        right = sum(candies) // k
        res = 0

        while left <= right:
            
            mid = (left + right) // 2

            count = 0

            for c in candies:
                if c >= mid:
                    count += c // mid
                
            if count >= k:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res