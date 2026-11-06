class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set([])
        for num in nums:
            hash.add(num)

        # at num i, check if num i - 1 is inside
        # if no then start checking for bigger items, if no then dont bother
        longest = 0
        for num in hash:
            if (num - 1 not in hash):
                i = 1
                while True:
                    if num + i not in hash:
                        if i > longest:
                            longest = i
                        break

                    else:
                        i += 1
        
        return longest
