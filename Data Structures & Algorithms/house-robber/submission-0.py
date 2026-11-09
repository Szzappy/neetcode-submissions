class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        prev1 = 0
        prev2 = 0

        for i in range(n):
            oldPrev = prev1
            prev1 = max(prev1, prev2 + nums[i])
            prev2 = oldPrev

        return prev1