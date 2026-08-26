class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        curSum=0

        for num in nums:
            curSum=max(curSum,0) # ensuring the curSum isn't negative
            curSum+=num
            maxSum=max(maxSum,curSum) # updating the maxSUm
        return maxSum