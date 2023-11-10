class Solution:
    def targetIndices(self, array: List[int], val: int) -> List[int]:

        # Applynormal binary search
        # But for detecting multiple elements,
        # Pop it from the array and start everything from starting
        # For that, just re-set start,end and mid pointers
        # Also as we are popping the items, keep a track of how many elements are popped
        # So, that we can add it to the index 
        # Because after popping, the elements in array decreases by 1 each time
        # So while pushing the index of target to the resultant array, we need to add the number of popped items till that point to get correct index
        
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
                p += 1        # Number of pop's
                start = 0
                end = len(array) - 1
                mid = (start + end) // 2
                
            
        l.sort()
        return l