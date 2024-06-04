class Solution:
    def occurrencesOfElement(self, nums: List[int], q: List[int], x: int) -> List[int]:
        
        res = []

        h = {i : [] for i in set(nums)}

        for i in range(len(nums)):
            h[nums[i]].append(i)

        for i in q:
            try: 
                res.append(h[x][i - 1])
            except:
                res.append(-1)

        return res