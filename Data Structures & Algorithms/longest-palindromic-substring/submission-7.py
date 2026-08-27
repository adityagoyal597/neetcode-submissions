class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0

        for i in range(len(s)):
            #even length
            L=i
            R=i

            while L>=0 and R<len(s) and s[L]==s[R]:
                if (R-L+1)>resLen:
                    resLen=R-L+1
                    res=s[L:R+1]
                L-=1
                R+=1

            L=i
            R=i+1

            while L>=0 and R<len(s) and s[L]==s[R]:
                if R-L+1>resLen:
                    resLen=R-L+1
                    res=s[L:R+1]
                L-=1
                R+=1
        return res