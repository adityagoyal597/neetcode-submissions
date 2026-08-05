class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        curComb=[]

        def dfs(i):
            if len(curComb)==k:
                res.append(curComb.copy())
                return 
            
            if i>n:
                return
            
            curComb.append(i)
            
            dfs(i+1)

            curComb.pop()

            dfs(i+1)
        
        dfs(1) # passing the starting value of n unlike in subset where we passed starting index 
        return res 