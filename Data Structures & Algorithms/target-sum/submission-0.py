from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(n, i):
            if i == len(nums):
                if n == target:
                    return 1
                else:
                    return 0

            return dfs(n + nums[i], i + 1) + dfs(n - nums[i], i + 1)
        
        return dfs(0, 0)
