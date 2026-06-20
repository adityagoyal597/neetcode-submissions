class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        
        dp=[1,1]
        i=2

        while i<=n:
            temp=dp[0]
            dp[0]=dp[0]+dp[1]
            dp[1]=temp
            i+=1
        return dp[0]

        