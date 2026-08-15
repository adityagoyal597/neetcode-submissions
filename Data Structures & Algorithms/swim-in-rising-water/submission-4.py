class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # grid
        N=len(grid)

        visit=set()
        minHeap=[]
        neighbors=[[1,0],[-1,0],[0,1],[0,-1]]
        visit.add((0,0))
        heapq.heappush(minHeap,(grid[0][0],0,0)) # val,row,col

        while minHeap:
            time,r,c=heapq.heappop(minHeap)

            if r==N-1 and c==N-1:
                return time

            for dr,dc in neighbors:
                nr,nc=r+dr,c+dc

                if 0<=nr<N and 0<=nc<N and (nr,nc) not in visit:
                    heapq.heappush(minHeap,(max(time,grid[nr][nc]),nr,nc))
                    visit.add((nr,nc))
        return 0
