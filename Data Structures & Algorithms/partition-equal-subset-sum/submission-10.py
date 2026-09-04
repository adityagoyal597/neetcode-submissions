class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)

        if total%2!=0:
            return False
        
        target=total//2

        cache={}

        def dfs(i,target):

            if target==0:
                return True
            if i>=len(nums) or target<0:
                return False
            
            if (i,target) in cache:
                return cache[(i,target)]
            
            take=dfs(i+1,target-nums[i])
            skip=dfs(i+1,target)

            cache[(i,target)]=take or skip

            return cache[(i,target)]

        return dfs(0,target)