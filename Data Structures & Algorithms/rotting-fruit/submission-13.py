class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # IN THIS QUESTION,SET ISN'T NEEDED AS WE R CHANGING IN PLACE
        
        freshFruits=0
        minutes=0
        neighbors=[[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS=len(grid),len(grid[0])
        queue=deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    freshFruits+=1
                if grid[r][c]==2:
                    queue.append((r,c))
        
        while queue and freshFruits:
            for _ in range(len(queue)):
                row,col=queue.popleft()

                for dr,dc in neighbors:
                    nr,nc=dr+row,dc+col

                    if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc]!=1:
                        continue
                    
                    # else
                    grid[nr][nc]=2
                    freshFruits-=1
                    queue.append((nr,nc))
            minutes+=1
        
        return -1 if freshFruits!=0 else minutes