class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result=0
        curSum=0

        prevSums={0:1}

        for num in nums:

            curSum+=num

            previousSum=curSum-k

            #if previousSum in prevSums:
            result+=prevSums.get(previousSum,0)

            prevSums[curSum]=1+prevSums.get(curSum,0)
        
        return result