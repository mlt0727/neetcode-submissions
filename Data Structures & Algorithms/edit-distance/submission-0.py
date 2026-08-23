class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m)]
        dp.append(list(range(n, -1, -1)))
        j = 0
        for i in range(m, -1, -1):
            dp[j][-1] = i
            j += 1
        

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if word2[r] == word1[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
        
        return dp[0][0]

