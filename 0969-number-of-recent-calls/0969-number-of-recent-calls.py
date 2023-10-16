class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue = self.queue
        start = t - 3000
        queue.append(t)
        
        while(queue and queue[0] < start):
            queue.popleft()

        return len(queue)

        # Just pop the items which sre less than t - 3000
        # Then, only past 3000 millin seconds requests
        # will be there