class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS=len(heights),len(heights[0])
        neighbors=[[1,0],[-1,0],[0,1],[0,-1]]
        pacific=set()
        atlantic=set()

        def dfs(r,c,visited,prevHeight):

            if r<0 or r>=ROWS or c<0 or c>=COLS:
                return 
            if (r,c) in visited:
                return 
            if heights[r][c]<prevHeight:
                return  
            
            visited.add((r,c))
            
            for dr,dc in neighbors:
                dfs(r+dr,c+dc,visited,heights[r][c])

        for c in range(COLS):
            dfs(0,c,pacific,heights[0][c])
        for r in range(ROWS):
            dfs(r,0,pacific,heights[r][0])
        
        for c in range(COLS):
            dfs(ROWS-1,c,atlantic,heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,COLS-1,atlantic,heights[r][COLS-1])
        
        res=[]

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res

        