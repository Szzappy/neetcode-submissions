class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(1, len(digits)):
            if digits[-i] == 10:
                digits[-i] = 0
                digits[-(i + 1)] += 1

            else:
                return digits

        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits