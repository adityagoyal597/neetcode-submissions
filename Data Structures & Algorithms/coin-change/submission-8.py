class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(i, amount):
            if amount == 0:
                return 0

            if i == len(coins) or amount < 0:
                return float("inf")

            if (i, amount) in cache:
                return cache[(i, amount)]

            # Include current coin
            include = 1 + dfs(i, amount - coins[i])

            # Skip current coin
            skip = dfs(i + 1, amount)

            cache[(i, amount)] = min(include, skip)

            return cache[(i, amount)]

        result = dfs(0, amount)

        return -1 if result == float("inf") else result