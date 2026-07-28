class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return_num = 0
        for num in nums:
            return_num ^= num

        return return_num