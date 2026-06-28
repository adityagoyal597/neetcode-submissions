class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        curSet=[]
        
        def helper(i,nums,curSet,result):
            if i>= len(nums):
                result.append(curSet.copy())
                return 
            
            # decision to include nums[i]
            curSet.append(nums[i])
            helper(i+1,nums,curSet,result)
            curSet.pop()

            # decision to not include nums[i]
            helper(i+1,nums,curSet,result)
        
        helper(0,nums,curSet,result)
        return result
