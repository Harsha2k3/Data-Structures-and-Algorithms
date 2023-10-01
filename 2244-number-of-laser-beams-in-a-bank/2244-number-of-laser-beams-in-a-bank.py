class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        res = 0
        prev = 0               # Number of lasers back side

        for i in bank:
            lasers = i.count('1')
            if lasers:  
                # If there are no lasers in a row, just skip it
                res += prev * lasers
                prev = lasers

        return res