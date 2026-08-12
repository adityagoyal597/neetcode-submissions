class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # starting from index i with curr sum total how many ways can we reach the target

        cache={} #(i,total)

        def dfs (i,curSum):
            if i==len(nums):
                if curSum==target:
                    return 1
                return 0
            
            if (i,curSum) in cache:
                return cache[(i,curSum)]

            add=dfs(i+1,curSum+nums[i])
            subtract=dfs(i+1,curSum-nums[i])

            cache[(i,curSum)]=add+subtract

            return cache[(i,curSum)]
        
        return dfs(0,0)
