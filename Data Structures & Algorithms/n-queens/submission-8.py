class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        positiveDiagonal=set() # r+c
        negativeDiagonal=set() # r-c

        res=[]

        board=[['.'] * n for i in range(n)]

        def backtrack(row):
            if row==n:
                copy=["".join(r) for r in board]
                res.append(copy)
                return
            
            for column in range(n):
                if column in col or (row+column) in positiveDiagonal or (row-column) in negativeDiagonal:
                    continue
                
                col.add(column)
                positiveDiagonal.add(row+column)
                negativeDiagonal.add(row-column)
                board[row][column]="Q"

                backtrack(row + 1)

                col.remove(column)
                positiveDiagonal.remove(row+column)
                negativeDiagonal.remove(row-column)
                board[row][column]="."
        
        backtrack(0)
        return res

