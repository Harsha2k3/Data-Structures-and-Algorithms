class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        # Just calculate which k-sized sub-array has least number 
        # of W's

        res = []
        w_count = blocks[:k].count("W")
        res.append(w_count)

        for i in range(1,len(blocks)-k+1):
            if(blocks[i-1+k] == "W"):
                w_count += 1
            if(blocks[i-1] == "W"):
                w_count -= 1

            res.append(w_count)

        return min(res)

        # For improving the code, we can just take a variable
        # w_count and when we are iterating over the windows of 
        # size k, if the item that is leaving the window is W,
        # then decrease w_count by 1 and if the item that is       entering the window is W, then increase the w_count by 1
        # Like, this in each window keep track of minimum W's  