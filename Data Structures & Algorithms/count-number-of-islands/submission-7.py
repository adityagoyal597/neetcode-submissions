class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        rows=len(grid)
        columns=len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]] # [up,down,right,left]

        def dfs(r,c):

            if r<0 or c<0 or r>=rows or c>=columns or grid[r][c]=="0":
                return 
            
            # else : grid[r][c]=1
            grid[r][c]="0"  # changing 1(land) to 0(water)

            for dr,dc in directions:
                dfs(r+dr,c+dc)
            
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]=="1":
                    dfs(i,j)
                    islands+=1
        
        return islands
