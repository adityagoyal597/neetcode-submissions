class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length=0
        L=0
        count={}

        for R in range(len(s)):
            count[s[R]]=1+count.get(s[R],0)

            while((R-L+1)-max(count.values())>k):
                count[s[L]]-=1
                L+=1
            # else no. of char to be replace < k
            length=max(length,R-L+1)
        return length