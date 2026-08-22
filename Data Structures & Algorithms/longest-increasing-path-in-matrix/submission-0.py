class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS,COLS=len(matrix),len(matrix[0])
        cache={}

        def dfs(r,c,prevVal):
            if (r<0 or r>=ROWS or c<0 or c>=COLS or matrix[r][c]<=prevVal):
                return 0
            
            if (r,c) in cache:
                return cache[(r,c)]

            res=1
            res=max(res,1+dfs(r+1,c,matrix[r][c])) 
            res=max(res,1+dfs(r-1,c,matrix[r][c])) 
            res=max(res,1+dfs(r,c+1,matrix[r][c])) 
            res=max(res,1+dfs(r,c-1,matrix[r][c])) 

            cache[(r,c)]=res
            return res

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row,col,-1)
        
        return max(cache.values())