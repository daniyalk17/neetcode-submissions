class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Assign left and right values
        left, right = 0, 1 # Left = buy, Right = Sell
        maxProfit = 0

        while right < len(prices): 
            # Profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit) 
            else:
                left = right

            right += 1
        return maxProfit

        
        