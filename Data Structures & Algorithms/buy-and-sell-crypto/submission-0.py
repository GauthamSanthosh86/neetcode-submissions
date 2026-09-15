class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p=prices[0]
        max_profit=0
        for i in prices:
            if i<min_p:
                min_p=i
            profit=i-min_p
            if profit>max_profit:
                max_profit=profit
        return max_profit
        
        