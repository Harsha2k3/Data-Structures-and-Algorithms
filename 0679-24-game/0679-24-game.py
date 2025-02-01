class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        def rec(cards):

            n = len(cards)

            if n == 1:
                if abs(cards[0] - 24) < 0.001:
                    return True
                return False

            for i in range(n):
                for j in range(i + 1 , n):
                    c1 = cards[i]
                    c2 = cards[j]

                    # Possible results
                    prs = [c1 + c2, c1 - c2, c2 - c1, c1 * c2] + ([c2 / c1] if c1 else []) + ([c1 / c2] if c2 else [])


                    for v in prs:
                        newcards = [v]


                        for k in range(n):
                            if k not in [i , j]:   # Because they are already used
                                newcards.append(cards[k])
                            
                        if rec(newcards):
                            return True
            
            return False

        return rec(cards)