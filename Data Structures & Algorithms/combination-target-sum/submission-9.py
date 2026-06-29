class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curComb=[]
        comb=[]

        def helper(i,target,curComb,comb):

            if target==0:
                comb.append(curComb.copy())
                return 
            
            if target<0:
                return 
            
            if i>=len(nums):
                return 
            
            # decision to include nums[i]
            curComb.append(nums[i])
            # passing i as the elements can be reused
            helper(i,target-nums[i],curComb,comb)
            curComb.pop()

            # decision to exclude nums[i]
            helper(i+1,target,curComb,comb)
        
        helper(0,target,curComb,comb)
        return comb
