class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        # First, pref[0] = arr[0]
        # Now, pref[1] = arr[0] ^ arr[1]
        # So, arr[1] = pref[1] ^ arr[0]
        # Now, pref[2] = arr[0] ^ arr[1] ^ arr[2]
        # So, arr[2] = pref[2] ^ (arr[0] ^ arr[1])

        arr = [pref[0]] * (len(pref))
        mul = arr[0]

        for i in range(1,len(pref)):
            arr[i] = pref[i] ^ mul
            mul = mul ^ arr[i]

        return arr