class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS,COLS=len(matrix),len(matrix[0])
        
        # All the values in sumMAtrix are initialized to zero initially
        self.sumMatrix=[[0]*(COLS+1) for row in range(ROWS+1)]

        for r in range(ROWS):
            # row wise prefix calculation
            prefix=0 
            for c in range(COLS):
                prefix+=matrix[r][c]
                # c+1 for offsetting the extra column which we added in the starting for boundary
                above=self.sumMatrix[r][c+1]
                # r+1 and c+! for offsetting the extar row and column which we added in starting of the sumMatrix for boundary check
                self.sumMatrix[r+1][c+1]=prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1

        bottomRight=self.sumMatrix[row2][col2]
        above=self.sumMatrix[row1-1][col2]
        left=self.sumMatrix[row2][col1-1]
        topLeft=self.sumMatrix[row1-1][col1-1]

        # as the topLeft is subtracted twice while subtracting above and left from bottom right
        # hence we add it once to omit error

        return bottomRight - above - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)