class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1

        while L<=R:

            mid=(L+R)//2

            if nums[mid]==target:
                return mid
            
            # left half sorted
            if nums[L]<=nums[mid]:

                # checking if the target is inside the sorted left half
                if nums[L]<=target<nums[mid]:
                    R=mid-1
                else:
                    L=mid+1
            
            # right half sorted
            else:

                # checking if the target is inside the sorted right half 
                if nums[mid]<target<=nums[R]:
                    L=mid+1
                else:
                    R=mid-1
        
        return -1 