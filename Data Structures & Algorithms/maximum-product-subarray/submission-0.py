class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1

        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            curmax, curmin = max(n * curmax, n * curmin, n), min(n * curmax, n * curmin, n)
            res = max(res, curmax)
        
        return res
