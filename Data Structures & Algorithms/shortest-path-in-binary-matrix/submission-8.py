class Solution:
    """
    Great observation – this is a third variant of grid BFS, but with a **different goal** than flood fill or number of islands. Let's break down the key differences and the reasoning behind each choice.

    ---

    ## 1. **Goal: shortest path vs. component connectivity**

    | Problem | Goal | Search method |
    |---------|------|---------------|
    | **Flood fill** | Change color of a connected region | BFS/DFS (any order – only need to visit all) |
    | **Number of islands** | Count connected components | BFS/DFS for each component |
    | **Shortest path (this problem)** | Find minimum number of steps from start to target | **BFS** only (guarantees shortest path in unweighted grid) |

    - In flood fill and num islands, **any traversal order** works because you only care about visiting every cell in the component.
    - In shortest path, you **must use BFS** (level‑by‑level) to ensure the first time you reach the target is via the shortest route. DFS would not be optimal.

    ---

    ## 2. **Directions: 4 vs. 8**

    - **Flood fill / num islands**: usually **4 directions** (up, down, left, right) – only side‑adjacent cells.
    - **Shortest path in binary matrix**: often **8 directions** (including diagonals) – each step counts as `1` even if moving diagonally.

    Your code uses `directions` with 8 entries. This is because the problem statement for *shortest path in a binary matrix* (LeetCode 1091) allows moving in all 8 directions.

    ---

    ## 3. **Visited tracking: grid modification vs. set**

    | Problem | How visited is tracked |
    |---------|------------------------|
    | **Flood fill** | Grid modified: `image[r][c] = color` (old value replaced) |
    | **Number of islands** | Grid modified: `grid[r][c] = "0"` |
    | **Shortest path** | **Separate visited set** `visit = set()` |

    ### Why the difference?

    - In flood fill and islands, you **are allowed to permanently change the grid** (the problem never needs the original values again). Changing the cell to a different value acts as an efficient visited marker without extra memory.
    - In shortest path, you **could** modify the grid (set `grid[r][c] = 1` after visiting) to avoid a visited set, and many solutions do that. However:
    - If the problem statement says you **cannot modify the input**, you must use a visited set.
    - Using a visited set is **safer** because it keeps the original grid unchanged, and it avoids any risk of accidentally interfering with other parts of the algorithm (though here it's fine).
    - Also, the visited set is **O(N²) in worst case**, same as the grid, so it's acceptable.

    **Your code uses a `visit` set** – that’s perfectly fine and often the clearest approach.

    ---

    ## 4. **Storing additional information in the queue**

    - **Flood fill / num islands**: queue stores only coordinates `(r, c)`.
    - **Shortest path**: queue stores `(r, c, length)` where `length` is the distance from the start.

    Because you need to return the **path length** when you first hit the target, you carry the distance with each BFS level. Alternatively, you could use a `dist` matrix, but the in‑queue approach is simpler.

    ---

    ## 5. **Early exit and bound checks**

    - **Flood fill**: only checks boundaries and color match.
    - **Number of islands**: no early exit – scans all cells.
    - **Shortest path**: two early exits:
    1. If start or target cell is `1` (blocked), return `-1` immediately.
    2. Inside the loop, if `(r,c)` is the target `(N-1, N-1)`, return `length` immediately.

    ---

    ## 6. **Return value**

    | Problem | Return |
    |---------|--------|
    | Flood fill | Modified grid |
    | Number of islands | Integer count |
    | Shortest path | Integer (shortest path length, or -1 if impossible) |

    ---

    ## Summary table

    | Aspect | Flood fill | Number of islands | Shortest path (binary matrix) |
    |--------|------------|-------------------|-------------------------------|
    | **Start** | Given `(sr, sc)` | Find all `'1'` cells | Given `(0,0)` (implicit) |
    | **Goal** | Paint region | Count islands | Min steps to `(N-1,N-1)` |
    | **Directions** | 4 | 4 | 8 (usually) |
    | **Visited** | Modify grid | Modify grid | Separate set (or modify grid) |
    | **Queue info** | `(r,c)` | `(r,c)` | `(r,c,dist)` |
    | **Search type** | DFS/BFS (any) | DFS/BFS (any) | BFS only (shortest path) |
    | **Early exit** | If `orig == color` | None | If start/target blocked; when target found |
    | **Return** | Modified grid | Count | `length` or `-1` |

    ---

    ## How to decide what to do in an OA?

    When you see a grid problem, ask yourself:

    1. **What is the goal?**
    - Change a region → flood fill.
    - Count regions → number of islands.
    - Find shortest distance → BFS + visited + level tracking.

    2. **Can I modify the grid?**
    - Yes → use grid as visited (saves memory).
    - No / want safety → use a visited set/array.

    3. **Do I need shortest path?**
    - Yes → BFS only. Store distance per node.
    - No → DFS/BFS either works.

    4. **Are moves only 4‑directional or 8**?
    - Read the problem statement carefully. For matrix problems, 4 is default, but some (like Knight moves, or this one) use 8.

    Your code is perfectly structured for the shortest path problem. The only possible improvement is that you could avoid the visited set by setting `grid[r][c] = 1` when you visit – but the set is cleaner and more explicit.

    Let me know if you’d like to see how the same code would look using grid modification instead of a set!
    """
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

            if r==N-1 and c==N-1: # reached the bottom rightmost cell 
                return length

            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<N and 0<=nc<N and grid[nr][nc]==0 and (nr,nc) not in visit:
                    queue.append((r+dr,c+dc,length+1))
                    visit.add((r+dr,c+dc))
        return -1