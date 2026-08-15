class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        queue=deque()
        fresh=0
        minutes=0
        neighbors=[[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    queue.append((r,c))
        
        while queue and fresh>0:

            for _ in range (len(queue)):
                row,col=queue.popleft()

                for dr,dc in neighbors:
                    nr,nc=row+dr,col+dc

                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        
                        queue.append((nr,nc))
                        
                        fresh-=1
            minutes+=1
        
        return minutes if fresh==0 else -1
                        

