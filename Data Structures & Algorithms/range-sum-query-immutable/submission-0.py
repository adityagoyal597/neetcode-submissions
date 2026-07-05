class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        total=0
        for num in nums:
            total+=num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        rightSum=self.prefix[right]

        if left>0: # left not equal to 0
            leftSum=self.prefix[left-1]
        else: # left equal to zero then subtract 0 from rightSum as leftSum of first element is 0
            leftSum=0 
        
        return rightSum-leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)