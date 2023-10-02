class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        window = arr[:k]
    
        # Iterate through the remaining elements
        for i in range(k, len(arr)):
            # Check if the current element is closer to x than the edge element of the window
            if abs(arr[i] - x) < abs(window[0] - x) or (abs(arr[i] - x) == abs(window[0] - x) and arr[i] < window[0]):
                # Update the sliding window
                window.pop(0)
                window.append(arr[i])
        
        return window