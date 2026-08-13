class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")]*(amount+1)
        # dp[a] = minimum number of coins required to make amount a.
        dp[0]=0
        # To make amount 0, we need 0 coins.

        for amt in range(1,amount+1):
            for coin in coins:
                if amt>=coin:
                    dp[amt]=min(dp[amt],1+dp[amt-coin])
        
        if dp[amount]==float('inf'):
            return -1
        else:
            return dp[amount]