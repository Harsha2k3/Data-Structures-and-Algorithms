class Solution:
    def targetIndices(self, array: List[int], val: int) -> List[int]:
        
        array.sort()

        start = 0
        end = len(array) - 1

        l = []
        p = 0

        mid = (start + end) // 2
        
        while(start <= end):
            if(val < array[mid]):
                end = mid - 1
            else:
                start = mid + 1
            
            mid = (start + end) // 2

            if(array[mid] == val):
                l.append(array.index(array[mid]) + p)
                array.pop(mid)
                p += 1
                start = 0
                end = len(array) - 1
                mid = (start + end) // 2
                
            
        l.sort()
        return l