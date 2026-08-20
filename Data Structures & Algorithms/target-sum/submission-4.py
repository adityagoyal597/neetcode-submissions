class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # starting from index i with curr sum total how many ways can we reach the target

        cache={} #(i,total)

        def dfs (i,curSum):
            if i==len(nums):
                if curSum==target:
                    return 1
                else:
                    return 0
            
            if (i,curSum) in cache:
                return cache[(i,curSum)]
            # adding 
            add=dfs(i+1,curSum+nums[i])
            # subtracting
            subtract=dfs(i+1,curSum-nums[i])

            cache[(i,curSum)]=add+subtract

            return cache[(i,curSum)]
        
        return dfs(0,0)
