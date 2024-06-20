class Solution:
    def maximumEnergy(self, energy , k):
       
        for i in range(k, len(energy)):
            energy[i] = max((energy[i] + energy[i - k]), energy[i])

        maxi = float("-inf")
        
        for i in range(len(energy) - k , len(energy)):
            maxi = max(maxi, energy[i])

        return maxi 