class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        window = arr[:k]
    
        # Iterate through the remaining elements
        for i in range(k, len(arr)):
            # Check if the current element(element that is enetering the window) is closer to x than the left edge element of the window
            if abs(arr[i] - x) < abs(window[0] - x) or (abs(arr[i] - x) == abs(window[0] - x) and arr[i] < window[0]):
                # Update the sliding window
                window.pop(0)
                window.append(arr[i])
        
        return window

        # We know that the sub-array should be contiguous of size k
        # So, use fixed sized sliding window of size k
        # As any how the array is sorted, we can grab k closest 
        # elements by just checking if the current element is closer to x than the edge element of the window and if the condition satisfies, just move the window