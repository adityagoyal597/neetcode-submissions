class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L,R=0,len(matrix[0])-1

        while L<R:
            for i in range(R-L):
                top,bottom=L,R

                topLeft=matrix[top][L+i]

                matrix[top][L+i]=matrix[bottom-i][L]

                matrix[bottom-i][L]=matrix[bottom][R-i]

                matrix[bottom][R-i]=matrix[top+i][R]

                matrix[top+i][R]=topLeft

            R-=1
            L+=1