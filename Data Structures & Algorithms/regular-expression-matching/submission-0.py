class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache={}

        def dfs(i,j):
            
            if j==len(p): # reached end of the pattern
                return i==len(s) #n true only if reached end of the string

            if(i,j) in cache: #memoization
                return cache[(i,j)]

            match=i<len(s) and(s[i]==p[j] or p[j]==".") # checking current char match
            if (j+1)<len(p) and p[j+1]=="*":
                #checking the next pattern char
                cache[(i,j)]=(
                    dfs(i,j+2) # ignore x*
                    or
                    (match and dfs(i+1,j)) # using x* again if current char match
                )
                return cache[(i,j)]
            if match: # no *
                cache[(i,j)]=dfs(i+1,j+1) # moving both ptrs ahead if current char match
                return cache[(i,j)]
            
            cache[(i,j)]=False
            return False
        
        return dfs(0,0)



            

