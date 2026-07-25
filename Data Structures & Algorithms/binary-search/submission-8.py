class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1


        while lower <= upper:
            midpoint = (lower + upper) // 2

            if target == nums[midpoint]:
                return midpoint

            elif target < nums[midpoint]:
                upper = midpoint - 1

            else:
                lower = midpoint + 1

        return -1