class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length=0
        L=0
        charCount={}

        for R in range(len(s)):
            # gets the previous value of key s[R] if not present initializes it to 0 and adds 1
            charCount[s[R]]=1+charCount.get(s[R],0)

            # checking the condition where all the least frequent characters in the window can't be replaced
            # no. of least frequent characters are more than the replacement allowed   
            # length of window - most frequent character <= k for replacement
            while ( (R-L+1) - max(charCount.values()) ) > k:
                charCount[s[L]]-=1
                L+=1
            
            length=max(length,R-L+1)
        
        return length