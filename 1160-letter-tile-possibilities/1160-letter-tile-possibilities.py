class Solution:
    def numTilePossibilities(self, nums: str) -> int:

        s = set()

        def rec(l , h):

            s.add("".join(l))

            if len(l) == len(nums):
                return 

            for i in range(len(nums)):
                if not h[i]:
                    l.append(nums[i])
                    h[i] = 1
                    rec(l , h)
                    l.pop()
                    h[i] = 0

        rec([] , [0] * len(nums))

        return len(s) - 1