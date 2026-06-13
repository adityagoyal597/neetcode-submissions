class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #n*n matrix , rows=columns
        
        N=len(grid)

        if grid[0][0] ==1 or grid[N-1][N-1]==1:
            return -1
        
        queue=deque()
        visit=set()

        queue.append((0,0,1)) #row,column,length
        visit.add((0,0))

        directions=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
        while queue:
            r,c,length=queue.popleft()

            if r==N-1 and c==N-1:
                return length

            for dr,dc in directions:
                if r+dr<0 or r+dr>=N or c+dc<0 or c+dc>=N or (r+dr,c+dc) in visit or grid[r+dr][c+dc]==1:
                    continue
                queue.append((r+dr,c+dc,length+1))
                visit.add((r+dr,c+dc))
        return -1