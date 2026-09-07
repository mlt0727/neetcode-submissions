from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        @cache
        def dfs(l, r):
            if l + 1 == r:
                return 0
            cur = 0
            for i in range(l + 1, r):
                cur = max(cur, dfs(l, i) + dfs(i, r) + nums[l] * nums[i] * nums[r])
            return cur
        return dfs(0, n - 1)

                
