class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()

        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:
                    triplets.add(tuple([nums[i], nums[start], nums[end]]))
                    start += 1

                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1

                elif nums[i] + nums[start] + nums[end] > 0:
                    end -= 1

        return list(triplets)