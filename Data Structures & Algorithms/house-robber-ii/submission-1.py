class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]

        prev1 = 0
        prev2 = 0

        for i in range(n - 1):
            oldPrev = prev1
            prev1 = max(prev1, prev2 + nums[i])
            prev2 = oldPrev

        dp1 = prev1

        prev1 = 0
        prev2 = 0

        for i in range(1, n):
            oldPrev = prev1
            prev1 = max(prev1, prev2 + nums[i])
            prev2 = oldPrev

        return max(dp1, prev1)