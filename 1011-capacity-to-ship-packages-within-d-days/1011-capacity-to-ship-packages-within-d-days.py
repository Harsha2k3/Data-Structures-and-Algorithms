class Solution:

    def days_req(self,cap,w):   # cap ==> capacity
        
        current_capacity = 0
        days = 0

        for i in w:
            if current_capacity + i <= cap:
                current_capacity += i
            else:
                days += 1
                current_capacity = i

        return days + 1  # Add 1 to account for the last day

    def shipWithinDays(self, w: List[int], d: int) -> int:
        
        left = max(w)
        right = sum(w)

        res = float("inf")

        while(left <= right):

            mid = (left + right) // 2

            if(self.days_req(mid,w) <= d):
                res = min(res,mid)
                right = mid - 1

            else:
                # We should increase the capacity to decrease the no.of days required
                left = mid + 1

        return res