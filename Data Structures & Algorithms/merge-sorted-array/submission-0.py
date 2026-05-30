class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m
        for num in nums2:
            nums1[i]=num
            j=i-1
            while(j>=0 and nums1[j]>nums1[j+1]):
                temp=nums1[j]
                nums1[j]=nums1[j+1]
                nums1[j+1]=temp
                j-=1
            i+=1

        