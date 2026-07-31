class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid

            print(l, r)

        final = nums[r] if nums[l] > nums[r] else nums[l]
        return final

            