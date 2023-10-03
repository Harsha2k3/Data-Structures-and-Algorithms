class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        # Just calculate which k-sized sub-array has least number 
        # of W's

        sub_arr = blocks[:k]
        count = float("inf")
        count = min(count,sub_arr.count("W"))

        for i in range(1,len(blocks)-k+1):
            count = min(count,blocks[i:k+i].count("W"))

        return count