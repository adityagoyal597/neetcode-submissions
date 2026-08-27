class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS,COLS=len(grid),len(grid[0])
        neighbors=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
        visit=set()

        def bfs(r,c):
            queue=deque()
            queue.append((r,c))
            visit.add((r,c))

            length=1
            while queue:

                for _ in range(len(queue)):
                    row,col=queue.popleft()

                    if row==ROWS-1 and col==COLS-1:
                        return length

                    for dr,dc in neighbors:
                        nr,nc=dr+row,dc+col

                        if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or (nr,nc) in visit or grid[nr][nc]==1:
                            continue
                        queue.append((nr,nc))
                        visit.add((nr,nc))
                length+=1
            return -1

        return bfs(0,0)

