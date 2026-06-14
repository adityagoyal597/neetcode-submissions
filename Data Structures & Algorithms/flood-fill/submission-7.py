class Solution:

    """
    Here, both problems are already solved without a visited set:

    Reprocessing is prevented by the pixel color check.
    The BFS only adds a neighbor if image[nr][nc] == orig. Once we change that neighbor to color, 
    its value no longer equals orig. So even if we later reach it again from another path, the 
    condition image[nr][nc] == orig will be False, and it won’t be added to the queue again.

    Infinite loops are impossible because we change the color exactly once per pixel, and we never change 
    it back to orig.
    Exception: If color == orig, we return the image immediately at the top of the function, so no BFS runs at all.

    Thus, a separate visited set would be redundant—the pixel value itself serves as the visitation marker.

    What each part does

    Setup
    orig = image[sr][sc]
    if orig == color:
        return image
    Saves the original color of the starting pixel.
    If it already matches the target color, no work is needed (early exit).

    BFS initialization
    m, n = len(image), len(image[0])
    q = deque([(sr, sc)])
    image[sr][sc] = color   # change starting pixel
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    m, n: dimensions of the image.

    q: a queue (FIFO) that stores coordinates of pixels that have been changed but whose neighbors still 
    need to be explored.
    We change the starting pixel immediately to color.
    dirs gives the four adjacent directions (down, up, right, left).

    Main loop
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == orig:
                image[nr][nc] = color
                q.append((nr, nc))
    Pop the front of the queue (r,c).
    For each neighbor (nr,nc):
    Bounds check.
    If the neighbor still has the original color (i.e., hasn't been filled yet), change it to color and push it 
    into the queue.
    This continues until no more pixels of orig remain adjacent to any filled pixel.

    Role of the queue
    Order of processing: BFS explores pixels layer by layer (like concentric rings). This is not required for 
    correctness (DFS would also work), but BFS often avoids deep recursion stack issues and can be easier 
    to reason about for flood fill.
    Stores work to do: Each pixel that gets changed is added to the queue so its neighbors will be examined later. 
    Without a queue (or stack), you wouldn't know which pixels still need to be expanded.
    Example walkthrough
    Given image = [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2.

    orig=1, color=2, no early exit.
    Change (1,1) to 2, queue = [(1,1)].
    Pop (1,1). Neighbors: (2,1) is 0 (skip), (0,1) is 1 → change to 2, push; (1,2) is 0 (skip); (1,0) is 1 → change to 2, push.
    Queue: [(0,1), (1,0)].
    Pop (0,1). Neighbors: (1,1) is already 2 (skip), (-1,1) out of bounds, (0,2) is 1 → change to 2, push; (0,0) is 1 → change to 2, push.
    Queue: [(1,0), (0,2), (0,0)].
    Pop (1,0). Neighbor (0,0) already changed, (2,0) is 0 (skip), (1,-1) invalid, (1,1) already changed. No new pushes.
    Pop (0,2). Only neighbor (1,2) is 0 (skip), rest invalid. Nothing new.
    Pop (0,0). All neighbors already changed or invalid. Queue empty.
    Return modified image.

    Time & Space Complexity
    Time: O(m × n) — each pixel is processed at most once (changed once).
    Space: O(m × n) in the worst case, because the queue can hold up to all pixels (e.g., all pixels same color as orig). The recursion call stack for DFS would also be O(m×n) in worst case (if deep recursion hits stack limit), so BFS is generally safer.
    """ 

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            
            original = image[sr][sc] # original color
            
            if original==color:
                return image
            
            # else original != color
            image[sr][sc]=color # then chnage the color to the desired color
            rows=len(image)
            columns=len(image[0])
            queue=deque()
            queue.append((sr,sc))
            directions=[[1,0],[-1,0],[0,1],[0,-1]]

            while queue:
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc

                    if 0<=nr<rows and 0<=nc<columns and image[nr][nc]==original:

                        image[nr][nc]=color
                        queue.append((nr,nc))
            return image
