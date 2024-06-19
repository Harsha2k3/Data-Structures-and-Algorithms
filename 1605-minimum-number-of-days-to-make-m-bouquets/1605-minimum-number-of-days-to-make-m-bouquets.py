class Solution:

    def isPossible(self,day,b,k,m):
          
        cnt = 0
        noOfB = 0     # Number of bouquets
        
        for i in range(len(b)):
            if b[i] <= day:
                cnt += 1
            else:
                noOfB += cnt // k
                cnt = 0

        noOfB += cnt // k

        return noOfB >= m


    def minDays(self, b: List[int], m: int, k: int) -> int:
        
        if((m * k) > len(b)):
            return -1

        left = min(b)
        right = max(b)

        r = float("inf")

        while(left <= right):

            mid = (left + right) // 2

            if(self.isPossible(mid,b,k,m)):
                r = min(r,mid)
                right = mid - 1
            
            else:
                left = mid + 1
        
        return r