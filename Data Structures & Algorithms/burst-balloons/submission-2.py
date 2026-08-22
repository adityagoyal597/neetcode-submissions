class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]

        cache={}

        def dfs(l,r):
            if l>r:
                return 0 # nothing to burst
            if (l,r) in cache:
                return cache[(l,r)]
            
            cache[(l,r)]=0

            for i in range(l,r+1): # trying evry baloon as the last baloon to burst
                coins=nums[l-1]*nums[i]*nums[r+1]
                coins+=dfs(l,i-1)+dfs(i+1,r)
                cache[(l,r)]=max(cache[(l,r)],coins)
            return cache[(l,r)]
        
        return dfs(1,len(nums)-2)