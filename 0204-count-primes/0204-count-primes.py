import math as m
class Solution:
    def countPrimes(self, n: int) -> int:

        if(n <= 2):
            return 0
        
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False
        
        for i in range(2,int(m.sqrt(n))+1):
            if(is_prime[i]):
                for j in range(2*i,n,i):    # We will start from next multiple of i so, 2*i and we will assign False with incrementing by i
                    is_prime[j] = False
                    
        return len([i for i in range(n) if is_prime[i]])