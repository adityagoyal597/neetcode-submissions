class Solution:
    def countSubstrings(self, s: str) -> int:
        result=0

        for i in range(len(s)):
            # odd length
            L,R=i,i

            while L>=0 and R<len(s) and s[L]==s[R]:
                result+=1
                L-=1
                R+=1

            # even length
            L,R=i,i+1
            while L>=0 and R<len(s) and s[L]==s[R]:
                result+=1
                L-=1
                R+=1
        
        return result