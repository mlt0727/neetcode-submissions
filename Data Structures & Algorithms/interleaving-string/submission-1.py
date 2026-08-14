from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 + n2 != len(s3):
            return False

        @cache
        def dfs(i1, i2, i3):
            if i1 == n1 and i2 == n2:
                return True
            res = False
            if i1 < n1 and s1[i1] == s3[i3]:
                res = res or dfs(i1 + 1, i2, i3 + 1)
            if i2 < n2 and s2[i2] == s3[i3]:
                res = res or dfs(i1, i2 + 1, i3 + 1)
            return res
        
        return dfs(0,0,0)

