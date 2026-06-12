class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,columns=len(grid),len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=columns or grid[r][c]==0:
                return 0
            
            grid[r][c]=0
            area=1
            for dr,dc in directions:
                area+=dfs(r+dr,c+dc)
            
            return area

        maxArea=0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==1:
                    maxArea=max(maxArea,dfs(i,j))
        
        return maxArea
