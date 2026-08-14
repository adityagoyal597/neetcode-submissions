class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]

        nums.sort()

        for i,firstNumber in enumerate(nums):

            # as the array is sorted if firstNumber becomes positive , all the numbers in the sorted array sfter it will also be positve 
            # triplet of positive numbers can't be 0
            
            if firstNumber>0:
                break
            
            # to skip duplicate triplet answers for duplicate firstNumber

            if firstNumber==nums[i-1] and i>0:
                # i>0 for first element
                continue

            L,R=i+1,len(nums)-1

            while L<R:
                threeSum=firstNumber+nums[L]+nums[R]

                # 2 Sum 2 problem
                if threeSum>0:
                    R-=1
                elif threeSum<0:
                    L+=1
                else:
                    # threeSum==0
                    result.append([firstNumber,nums[L],nums[R]])

                    # searching for another pair
                    L+=1
                    R-=1


                    # skipping duplicates for the secondNumber which will lead to the same answer
                    while nums[L]==nums[L-1] and L<R:
                        L+=1
        
        return result

