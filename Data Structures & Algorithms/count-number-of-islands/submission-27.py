class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        neighbors=[[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS=len(grid),len(grid[0])
        visit=set()

        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visit or grid[r][c]=="0":
                return

            visit.add((r,c)) 
            
            for dr,dc in neighbors:
                nr,nc=dr+r,dc+c
                dfs(nr,nc)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1" and (r,c) not in visit:
                    dfs(r,c)
                    islands+=1
        
        return islands
            
            