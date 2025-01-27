class Solution:
    def numTilePossibilities(self, nums: str) -> int:

        s = set()

        def rec(l , h):

            if "".join(l): s.add("".join(l)) 

            for i in range(len(h)):
                if not h[i]:
                    l.append(nums[i])
                    h[i] = 1
                    rec(l , h)
                    l.pop()
                    h[i] = 0
        
        rec([] , [0] * len(nums))

        return len(s)