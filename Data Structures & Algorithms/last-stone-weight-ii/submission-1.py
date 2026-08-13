class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum=sum(stones)

        target=math.ceil(stoneSum/2)

        cache={}

        def dfs(i,total):
            if total>=target or i==len(stones):
                return abs(total-(stoneSum-total))
            if(i,total) in cache:
                return cache[(i,total)]
            
            cache[(i,total)]=min(
                dfs(i+1,total+stones[i]), # including
                dfs(i+1,total) # not including
            )

            return cache[(i,total)]
        
        return dfs(0,0)
        
