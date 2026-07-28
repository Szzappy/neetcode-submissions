class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        expected = 0.5 * (len(nums) + 1) * len(nums)

        return int(expected - total)
