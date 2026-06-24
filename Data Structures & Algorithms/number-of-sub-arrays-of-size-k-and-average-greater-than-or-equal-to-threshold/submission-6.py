class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum=0
        count=0
        L=0

        # subarray of size k -> no. of elements in window is k 

        for R in range(len(arr)):
            curSum+=arr[R]

            # no. of elements in window exceeds k
            if R-L+1>k:
                curSum-=arr[L]
                L+=1
            
            # no. of elements in window equal to k
            if R-L+1==k:
                # if (curSum/k) >= threshold:
                if curSum >= k*threshold:
                    count+=1
        
        return count


            