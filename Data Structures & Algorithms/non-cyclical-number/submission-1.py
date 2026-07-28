class Solution:
    def isHappy(self, n: int) -> bool:
        revisited = {}
        num_sum = n

        while num_sum != 1:
            n_str = str(num_sum)
            temp = 0

            for num in n_str:
                temp += (int(num) * int(num))

            if temp in revisited:
                return False

            revisited[temp] = 1
            num_sum = temp
        
        return True