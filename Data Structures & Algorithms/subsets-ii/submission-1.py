class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subSet=[]
        curSet=[]
        # sort the array with duplicated elements
        nums.sort()

        def helper(i,nums,curSet,subSet):

            if i>=len(nums):
                subSet.append(curSet.copy())
                return 
            
            # decision to include nums[i]
            curSet.append(nums[i])
            helper(i+1,nums,curSet,subSet)
            curSet.pop()

            # decision to exclude all the duplicate values of nums[i]

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            helper(i+1,nums,curSet,subSet)
        
        helper(0,nums,curSet,subSet)
        return subSet