class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        curComb=[]

        def dfs(i,total):
            if total== target:
                res.append(curComb.copy())
                return 
            
            if i>=len(nums) or total>target:
                return
            
            curComb.append(nums[i])

            dfs(i,total+nums[i])
            curComb.pop()
            dfs(i+1,total)

        dfs(0,0)
        return res