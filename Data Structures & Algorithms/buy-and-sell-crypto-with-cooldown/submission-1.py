from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                return max(cooldown, buy)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                return max(cooldown, sell)

        return dfs(0, True)