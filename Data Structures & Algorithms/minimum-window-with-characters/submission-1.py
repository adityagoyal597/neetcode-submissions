class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        
        countT={}
        window={}

        for c in t:
            countT[c]=1+countT.get(c,0)
        
        have , need = 0,len(countT)
        res=[-1,-1]
        resLen=float("inf")
        L=0

        for R in range(len(s)):
            c=s[R]
            window[c]=1+window.get(c,0)

            if c in countT and window[c]==countT[c]:
                have+=1
            
            while have==need:
                if(R-L+1)<resLen:
                    res=[L,R]
                    resLen=R-L+1
                
                window[s[L]]-=1

                if s[L] in countT and window[s[L]]<countT[s[L]]:
                    have-=1
                L+=1
        l, r = res
        return s[l:r+1] if resLen!=float("inf") else ""