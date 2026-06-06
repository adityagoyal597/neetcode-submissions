class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(i,cur,sum):
            if sum==target:
                res.append(cur.copy())
                return

            if sum>target or i>=len(nums):
                return
            
            cur.append(nums[i])
            dfs(i,cur,sum+nums[i])
            cur.pop()
            dfs(i+1,cur,sum)
        
        dfs(0,[],0)
    
        return res