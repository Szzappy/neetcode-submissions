class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
                continue

            totalProd *= num

        for i in range(len(nums)):
            if zeroCount > 1 or zeroCount == 1 and nums[i] != 0:
                nums[i] = 0
            else:
                nums[i] = totalProd // (nums[i] if nums[i] != 0 else 1)

        return nums