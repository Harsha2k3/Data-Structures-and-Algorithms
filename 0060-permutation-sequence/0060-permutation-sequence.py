class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # Backtracking solution gives TLE

        # nums = [str(i) for i in range(1 , n + 1)]
        
        # res = []

        # vis = [0] * n

        # def rec(ind , l , nums , vis , k):

        #     if len(l) == n:
        #         res.append(l.copy())
            
        #     for i in range(len(vis)):
        #         if not vis[i]:
        #             l.append(nums[i])
        #             vis[i] = 1
        #             rec(i + 1 , l , nums , vis , k)
        #             vis[i] = 0
        #             l.pop()

        # rec(0 , [] , nums , vis , k)

        # return "".join(res[k - 1])


        fact = 1

        numbers = []

        for i in range(1, n):
            fact *= i
            numbers.append(i)

        numbers.append(n)

        ans = ""
        k -= 1

        while True:
            ans += str(numbers[k // fact])
            numbers.pop(k // fact)
            if not numbers:
                break
            k %= fact
            fact //= len(numbers)
            
        return ans