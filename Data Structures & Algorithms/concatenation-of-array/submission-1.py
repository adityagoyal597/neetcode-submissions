class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size=len(nums)
        ans=[0]*2*size
        for i,num in enumerate(nums):
            ans[i]=nums[i]
            ans[i+size]=nums[i]
        return ans
        