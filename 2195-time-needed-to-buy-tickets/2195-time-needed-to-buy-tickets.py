class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        secs = 0 
        i = 0
        while tickets[k] != 0:
            if tickets[i] != 0: 
                tickets[i] -= 1 
                secs += 1 

            i = (i + 1) % len(tickets) 
            
        return secs