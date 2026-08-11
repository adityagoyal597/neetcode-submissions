class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total=sum(nums)

        # total must be equal for it to divide evenly between two subsets
        if total%2!=0:
            return False
        
        # even sum
        target=total//2

        cache=[]

        for i in range(len(nums)):
            cache.append([-1]*(target+1))
        
        # cache[i][target]-> calculated whether we can create this target using elemets starting from i

        def memoHelper(i,capacity):
            if capacity==0:
                return True
            if i==len(nums):
                return False
            if cache[i][capacity]!=-1:
                return cache[i][capacity]
            
            # choice-1) skip the number
            skip=memoHelper(i+1,capacity)

            #choice-2) 
            take=False

            if nums[i]<=capacity:
                take=memoHelper(i+1,capacity-nums[i])
            
            cache[i][capacity]=skip or take

            return cache[i][capacity]
        
        return memoHelper(0,target)
        