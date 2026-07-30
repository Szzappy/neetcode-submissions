class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freqs = {}

        for num in nums:
            if num not in num_freqs:
                num_freqs[num] = 0

            num_freqs[num] += 1

        print(num_freqs)

        list_freqs = list(num_freqs.items())
        print(list_freqs)

        k_freqs = []

        for val in list_freqs:
            heapq.heappush(k_freqs, (val[1], val[0]))

            if len(k_freqs) > k:
                heapq.heappop(k_freqs)

        print(k_freqs)
        returnVal = []
        for val in k_freqs:
            returnVal.append(val[1])

        return returnVal