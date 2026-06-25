class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L=0
        R=1
        length=1
        prev=""

        while R<len(arr):
            if arr[R-1]<arr[R] and prev != "<":
                length=max(length,R-L+1)
                R+=1
                prev="<"
            elif arr[R-1]>arr[R] and prev !=">":
                length=max(length,R-L+1)
                R+=1
                prev=">"
            else:
                R=R+1 if arr[R-1]==arr[R] else R
                L=R-1
                prev=""
            
        return length
