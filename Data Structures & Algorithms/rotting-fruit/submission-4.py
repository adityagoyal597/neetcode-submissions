class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        time=0
        freshFruits=0
        queue=deque()

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j]==1:
                    freshFruits+=1
                elif grid[i][j]==2:
                    queue.append((i,j))

        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        while freshFruits and queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<ROWS and 0<=nc<COLUMNS and grid[nr][nc]==1:
                        queue.append((nr,nc))
                        grid[nr][nc]=2
                        freshFruits-=1
            time+=1
    
        return time if freshFruits==0 else -1