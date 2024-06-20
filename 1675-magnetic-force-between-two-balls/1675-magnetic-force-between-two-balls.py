class Solution(object):
    def maxDistance(self, p, m):

        def isPossible(mid , p , m):
            prev = p[0]
            m -= 1        # Ball at p[0] , so m -= 1

            for i in range(1 , len(p)):
                if p[i] - prev >= mid:
                    m -= 1
                    prev = p[i]
            
                if m == 0:
                    return True
            
            return False

        p.sort()

        left = 1              # Minimum possible magnetic force
        right = p[-1] - p[0]  # Maximum possible magnetic force

        res = left

        while left <= right:

            mid = (left + right) // 2

            if isPossible(mid , p , m):
                res = max(res , mid)
                left = mid + 1     
                # Try increasing the magnetic force
            
            else:
                right = mid - 1
        
        return res