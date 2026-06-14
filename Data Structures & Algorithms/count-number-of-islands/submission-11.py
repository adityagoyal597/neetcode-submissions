class Solution:
    """
    Great question! The `numIslands` and `floodFill` problems are very similar—both are **grid‑based connected component** problems using DFS/BFS. Let's walk through the key differences and then how to think during an online assessment.

    ---

    ## 1. Core Difference: **One component vs. all components**

    |                     | **floodFill** | **numIslands** |
    |---------------------|---------------|-----------------|
    | **Starting point**  | Given one cell `(sr, sc)` | You must **find** all cells that are `'1'` (by scanning the grid) |
    | **Goal**            | Change the **single component** containing the start to a new color | **Count** how many separate components of `'1'` exist |
    | **Visited marking** | Change pixel to the new `color` | Change `'1'` to `'0'` (or any marker) |
    | **Iteration**       | Only one BFS/DFS from the start | Loop over every cell; start a BFS/DFS when you find an unvisited `'1'` |

    In your `numIslands` code:
    - You **scan** the whole grid (`for r in range(ROWS): for c in range(COLS)`).
    - When you find a `'1'`, you start a BFS that changes **all cells in that island** to `'0'` (visited).
    - After the BFS finishes, you increment `islands` and continue scanning.
    - You never revisit those cells because they are now `'0'`.

    In `floodFill`:
    - You are given the starting cell **directly** – no scanning needed.
    - You only run one BFS/DFS from that cell.
    - You change the original color to the new `color`, but only for cells **connected** to the start that originally had the same color.

    ---

    ## 2. Why does `numIslands` need a double loop but `floodFill` doesn't?

    - **floodFill** asks: “Given a starting pixel, what does the connected region look like after the fill?”
    - **numIslands** asks: “How many separate connected regions of `'1'` exist in the entire grid?”

    If you only ran BFS from one random cell in `numIslands`, you would miss islands that are not connected to that cell. Hence the need to scan all cells.

    ---

    ## 3. Both avoid a separate visited set – why?

    Both problems modify the grid **in place** to mark visited cells:
    - floodFill: changes `orig` → `color`. After that, the cell no longer matches `orig`, so it won't be processed again.
    - numIslands: changes `'1'` → `'0'`. A `'0'` cell is never considered a starting point for a new island, and BFS only expands to `'1'` cells.

    This is efficient and uses O(1) extra space (besides the recursion stack/queue). You should **only do this if the problem allows modifying the input grid** – most online assessments do, but occasionally they might forbid it. If so, use a `visited` boolean matrix.

    ---

    ## 4. How to decide what to do in an online assessment?

    Here’s a mental checklist:

    ### Step 1: Understand the problem
    - **Am I given a start point?** → floodFill style (one component).
    - **Do I need to find something about all components?** → numIslands style.

    ### Step 2: Choose search algorithm (BFS vs DFS)
    - **floodFill**: both work. BFS is often simpler to implement iteratively. DFS recursion can hit stack limit if the grid is large (though constraints are < 50x50, so it's fine).
    - **numIslands**: same choice. BFS/DFS both accepted.

    ### Step 3: Decide how to mark visited
    - Can I modify the grid? Yes → just change the value.
    - No → use a `visited` set or boolean matrix (extra memory, but safe).

    ### Step 4: Handle edge cases
    - **floodFill**: If `image[sr][sc] == color`, return immediately (no changes). Also, if the grid is empty (but constraints say at least 1x1).
    - **numIslands**: If grid is empty, return 0. Also, check bounds when accessing neighbors.

    ### Step 5: Optimize for the constraints
    - Both `m,n <= 50` or `m,n <= 300`? BFS/DFS recursion is fine. Memory: store queue/stack of up to `m*n` entries, okay.
    - If grid is huge (e.g., 1000x1000), prefer iterative BFS to avoid recursion depth limits, and consider using a visited set if modifying grid is not allowed.

    ---

    ## 5. Quick comparison side-by-side

    | Aspect | floodFill | numIslands |
    |--------|-----------|------------|
    | **Input** | `image`, `sr`, `sc`, `color` | `grid` of chars |
    | **Start** | Given | Need to find |
    | **Loop over all cells?** | No | Yes |
    | **What changes?** | All connected cells of `orig` become `color` | All '1' become '0' (temporarily) |
    | **Return** | Modified grid | Integer count |
    | **Early exit** | If `orig == color`, return unchanged | N/A |
    | **Metric** | BFS from one point | BFS for each new island found |

    ---

    ## Example walkthrough for numIslands (your code)

    Grid:
    ```
    1 1 0
    0 1 0
    0 0 1
    ```

    1. Outer loop finds `(0,0)` = '1' → start BFS, change all connected '1's to '0'. Island count = 1.
    2. After BFS, grid becomes:
    ```
    0 0 0
    0 0 0
    0 0 1
    ```
    3. Continue scanning: `(0,1)` is now 0, skip; ... finally `(2,2)` is still 1 → new BFS, change it to 0. Island count = 2.
    4. Return 2.

    Notice: If we had **not** changed the grid in place, we would need a separate visited matrix, and the BFS starting from `(0,0)` would have to check visited for each neighbor – which is exactly what the grid value does.

    ---

    ## Final tip for OAs

    - **Practice writing both patterns** until they become muscle memory (BFS with `deque`, DFS with recursion or explicit stack).
    - **Read the problem carefully**: Does it say “**modify** the input grid” or “return a new 2D array”? If the latter, make a deep copy first.
    - **Test with small examples**, especially edge cases (single cell, already same color, all different colors, all same).

    """
    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        rows=len(grid)
        columns=len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def bfs(r,c):
            queue=deque()
            grid[r][c]="0" # changing the passed [row][column] land to water
            queue.append((r,c))

            while queue: ## continues as long there is no land wihtin all the neighbor 
                row,column=queue.popleft()
                for dr , dc in directions:
                    nr,nc=row+dr,column+dc

                    if 0<=nr<rows and 0<=nc<columns and grid[nr][nc]=="1": 
                        # checking if any of the neighbors are land
                        # yes- append it to the queue and make it water
                        queue.append((nr,nc))
                        grid[nr][nc]="0"
        
        for row in range(rows): ## checking all the land areas in the global grid
            for column in range(columns):
                if grid[row][column]=="1":
                    bfs(row,column)
                    islands+=1
        
        return islands



