class Solution:
    def reverseBits(self, n: int) -> int:
        binary = str(format(n, "032b"))
        flip = binary[::-1]

        return int(flip, 2)