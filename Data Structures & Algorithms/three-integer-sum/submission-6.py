class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]

        nums.sort()

        for i , firstNumber in enumerate(nums):
            if firstNumber>0:
                break
            
            if nums[i]==nums[i-1] and i>0:
                continue
            
            L=i+1
            R=len(nums)-1

            while L<R:

                threeSum=firstNumber+nums[L]+nums[R]

                if threeSum<0:
                    L+=1
                elif threeSum>0:
                    R-=1
                else:
                    res.append([firstNumber,nums[L],nums[R]])
                    L+=1
                    R-=1

                    while nums[L]==nums[L-1] and L<R:
                        L+=1
        
        return res