class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        queue=deque()
        visit=set()
        neighbors=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]

        if grid[0][0]==1 or grid[ROWS-1][COLS-1]==1:
            return -1
        
        queue.append((0,0))
        visit.add((0,0))

        length=1
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()

                if r==ROWS-1 and c==COLS-1:
                    return length
                
                for dr,dc in neighbors:
                    nr,nc=dr+r,dc+c
                    
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==0 and (nr,nc) not in visit:
                        queue.append((nr,nc))
                        visit.add((nr,nc))
            length+=1
        
        return -1