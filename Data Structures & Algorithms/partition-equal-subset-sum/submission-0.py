class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total//2

        num = set([0])

        for n in nums:
            cur = num.copy()
            for i in cur:
                if n + i == target:
                    return True
                num.add(n + i)
        
        return False

        
            