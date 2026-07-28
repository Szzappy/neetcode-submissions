class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        if len(stones) == 1:
            return stones[0]

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, first - second)

        last = heapq.heappop(heap) * -1 if len(heap) == 1 else 0

        return last