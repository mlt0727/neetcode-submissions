from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        @cache
        def dfs(r, c):
            cur = 1
            for mr, mc in direction:
                nr, nc = r + mr, c + mc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    cur = max(cur, dfs(nr, nc) + 1)
            return cur

        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
        return res
