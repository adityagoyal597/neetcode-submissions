class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        cache={}

        def dfs(i):
            if i in cache:
                return cache[i]
            
            LIS=1
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    LIS=max(LIS,1+dfs(j))
            
            cache[i]=LIS
            return LIS
            
        return max(dfs(i) for i in range(n))
    
