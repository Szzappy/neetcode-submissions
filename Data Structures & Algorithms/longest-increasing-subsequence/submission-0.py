class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        # dp[i] is the LIS up to index i
        # dp[0] = 1
        dp = [1] * n

        # looking at nums[i]
        for i in range(n):
            # compare nums i to nums[j]
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)