class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0,len(arr)-1):
            max=arr[i+1]
            for index in range(i+1,len(arr)):
                if arr[index]>max:
                    max=arr[index]
            arr[i]=max
        arr[len(arr)-1]=-1
        return arr
