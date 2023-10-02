class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice, maxProfit = float("inf"), float("-inf")

        for curr_price in prices:
            minPrice = min(minPrice,curr_price)
            maxProfit = max(maxProfit,(curr_price - minPrice))
        
        return maxProfit

# curr_price is the price on the day which we are selling the stock

# Traverse along the array
# In each iteration, store the minimum price encountered so far
# In each iteration, do max(curr_price-minimum price encountered so far)