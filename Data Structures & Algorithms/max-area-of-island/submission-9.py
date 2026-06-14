class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            queue=deque()
            grid[r][c]=0
            queue.append((r,c))
            area=1

            while queue:
                row,column=queue.popleft()
                for dr,dc in directions:
                    nr,nc=row+dr,column+dc
                    if 0<=nr<ROWS and 0<=nc<COLUMNS and grid[nr][nc]==1:
                        queue.append((nr,nc))
                        grid[nr][nc]=0
                        area+=1
            return area

        maxArea=0
        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column]==1:
                    maxArea=max(maxArea,bfs(row,column))
        
        return maxArea
