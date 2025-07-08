# Last updated: 7/8/2025, 10:15:44 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==sorted(prices):
            return prices[len(prices)-1]-prices[0]

        if prices==sorted(prices, reverse=True):
            return 0

        profit=0    

        for i in range(0,len(prices)):
            
            if i<len(prices)-1 and prices[i]<prices[i+1]:
                profit+=prices[i+1]-prices[i]
        return profit       

        