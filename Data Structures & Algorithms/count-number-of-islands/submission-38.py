class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        neighbors=[[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS=len(grid),len(grid[0])
        visit=set()

        def bfs(r,c):
            queue=deque()
            queue.append((r,c))
            visit.add((r,c))

            while queue:
                for _ in range (len(queue)):
                    row,col=queue.popleft()

                    for dr,dc in neighbors:
                        nr,nc=dr+row,dc+col

                        if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or (nr,nc) in visit or grid[nr][nc]=="0":
                            continue
                        queue.append((nr,nc))
                        visit.add((nr,nc))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands        
            