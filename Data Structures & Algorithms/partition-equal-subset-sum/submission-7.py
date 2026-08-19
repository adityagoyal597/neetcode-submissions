class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total=sum(nums)

        # total must be equal for it to divide evenly between two subsets
        if total%2!=0:
            return False
        
        # even sum
        target=total//2

        cache={}

        
        # cache[i][target]-> calculated whether we can create this target using elemets starting from i

        def dfs(i,target):
            if target==0:
                return True
            if i==len(nums) or target<0:
                return False
            if (i,target) in cache:
                return cache[(i,target)]
            
            # choice-1) skip the number
            skip=dfs(i+1,target)

            #choice-2) take yhe number
            take=dfs(i+1,target-nums[i])
            
            cache[(i,target)]=skip or take

            return cache[(i,target)]
        
        return dfs(0,target)
        