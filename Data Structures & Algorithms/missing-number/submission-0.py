class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0  1  3  6  10
        total = 0
        expected = 0.5 * (len(nums) + 1) * len(nums)
        for num in nums:
            total += num

        return int(expected - total)
