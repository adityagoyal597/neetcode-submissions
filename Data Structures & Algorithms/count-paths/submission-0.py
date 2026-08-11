class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #bottom row  has only one possible way to reach dest. as can't go bottom
        row=[1]*n

        # already intiatitated bottom row
        for i in range(m-1): # remaining m-1 rows
            newRow=[1]*n
            for j in range(n-2,-1,-1):
                newRow[j]=newRow[j+1]+row[j]
            row=newRow
        return row[0]
