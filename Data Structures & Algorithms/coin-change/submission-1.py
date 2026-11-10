class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if coins is None:
            return -1

        if amount == 0:
            return 0

        n = len(coins)

        # dp[i] is the minimum amount of coins for amount i
        dp = [math.inf] * amount

        for i in range(1, amount + 1):
            for j in range(n):
                if i == coins[j]:
                    dp[i - 1] = 1
                    break

                if coins[j] > i:
                    continue
                
                dp[i - 1] = min(dp[i - 1], dp[i - 1 - coins[j]] + 1)


        return dp[-1] if dp[-1] != math.inf else -1