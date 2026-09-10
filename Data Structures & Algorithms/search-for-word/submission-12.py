class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,columns=len(board),len(board[0])
        visit=set()

        def dfs(i,r,c):

            if i==len(word):
                return True
            
            if r<0 or r>=rows or c<0 or c>=columns or (r,c) in visit or board[r][c]!=word[i]:
                return False
            
            visit.add((r,c))

            result=(
                dfs(i+1,r+1,c) or
                dfs(i+1,r-1,c) or
                dfs(i+1,r,c+1) or 
                dfs(i+1,r,c-1)
            )


            visit.remove((r,c))
            return result
        
        for r in range(rows):
            for c in range(columns):
                if dfs(0,r,c):
                    return True
        return False