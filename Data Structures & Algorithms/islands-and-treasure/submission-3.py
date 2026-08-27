class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()

        neighbors= [(1,0),(-1,0),(0,1),(0,-1)]

        INF=2147483647

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 0: # treasure chest found
                    queue.append((r,c))

        while queue:

            r,c = queue.popleft()

            for dr,dc in neighbors:

                nr,nc= r+dr,c+dc

                if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==INF:
                    grid[nr][nc]=grid[r][c]+1
                    queue.append((nr,nc))