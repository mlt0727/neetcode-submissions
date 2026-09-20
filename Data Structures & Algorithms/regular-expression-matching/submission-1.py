from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if j >= len(p):
                if i >= len(s):
                    return True
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            cur = False
            if (j + 1) < len(p) and p[j + 1] == "*":
                cur = cur or dfs(i, j + 2)
                if match:
                    cur = cur or dfs(i + 1, j)
                return cur

            if match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)