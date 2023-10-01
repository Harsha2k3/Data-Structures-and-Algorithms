class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice, maxProfit = float("inf"), float("-inf")

        for curr_price in prices:
            minPrice = min(minPrice,curr_price)
            maxProfit = max(maxProfit,(curr_price - minPrice))
        
        return maxProfit

# curr_price is the price on the day which we are selling the stock

# Traverse prices once and at each position keep track of the min Price so far and max profit, profit = curr_price-min price