class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}

        def dfs(i,amount):
            if amount==0:
                return 1
            
            if i ==len(coins) or amount<0:
                return 0
            
            if (i,amount) in cache:
                return cache[(i,amount)]
            # include cureent coin
            include=dfs(i,amount-coins[i])
            # skip current coin
            skip=dfs(i+1,amount)

            cache[(i,amount)]=include+skip

            return cache[(i,amount)]
        
        return dfs(0,amount)
