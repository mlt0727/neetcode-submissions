class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]

        dp[0] = [1] * (len(coins) + 1)

        for r in range(1, amount + 1):
            for c in range(len(coins) - 1, -1, -1):

                dp[r][c] = dp[r][c + 1]

                if r - coins[c] >= 0:
                    dp[r][c] += dp[r - coins[c]][c]

        return dp[amount][0]