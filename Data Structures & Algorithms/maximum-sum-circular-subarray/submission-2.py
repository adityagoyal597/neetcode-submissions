class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax=nums[0]
        globalMin=nums[0]
        curMax=0
        curMin=0
        total=0

        for num in nums:
            total+=num
            curMax=max(curMax,0)
            curMin=min(curMin,0)
            curMax+=num
            curMin+=num
            globalMax=max(globalMax,curMax)
            globalMin=min(globalMin,curMin)
        
        return globalMax if globalMax<0 else max(globalMax,total-globalMin)