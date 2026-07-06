class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftSum=0
        for i in range(len(nums)):
            rightSum=total-leftSum-nums[i]

            if leftSum==rightSum:
                return i
            else: # leftSum not equal to rightSum
                leftSum+=nums[i]
        # no pivot index found
        return -1
        