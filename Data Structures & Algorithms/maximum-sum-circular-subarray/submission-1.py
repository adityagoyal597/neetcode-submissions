class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax,curMin=0,0
        globalMin,globalMax=nums[0],nums[0]
        total=0

        for num in nums:
            total+=num
            curMax=max(curMax+num,num)
            curMin=min(curMin+num,num)
            globalMin=min(globalMin,curMin)
            globalMax=max(globalMax,curMax)

        if globalMax<0:
            return globalMax
        return max(total-globalMin,globalMax)