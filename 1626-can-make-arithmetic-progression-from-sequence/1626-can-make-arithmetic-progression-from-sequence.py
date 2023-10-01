class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        res = False
        arr.sort()

        if(len(arr)>2):
            for i in range(len(arr)-2):
                if(arr[i]-arr[i+1] == arr[i+1]-arr[i+2]):
                    res = True
                else:
                    res = False
                    break
        else:
            res = True

        return res