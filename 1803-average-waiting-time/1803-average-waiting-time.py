class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        wait = cur = 0.
        for t , d in customers:
            cur = max(cur , t) + d
            wait += cur - t
        
        return wait / len(customers)