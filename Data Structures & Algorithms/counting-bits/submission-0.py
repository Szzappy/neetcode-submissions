class Solution:
    def countBits(self, n: int) -> List[int]:
        n += 1
        vals = [0] * n
        for num in range(n):
            for i in range (31):
                vals[num] += (num >> i) & 1

        return vals