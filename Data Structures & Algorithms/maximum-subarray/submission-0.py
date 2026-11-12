class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, 0
        cur = 0
        ans = 0
        while r < len(nums):
            cur += nums[r]
            ans = max(ans, cur)
            if cur < 0:
                l = r
                cur = 0
            r += 1
        
        return ans if ans != 0 else max(nums)