class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result=0
        L=0
        R=len(heights)-1

        while L<R:
            area= (R-L) * min(heights[L],heights[R])
            result=max(result,area)

            # maximazing the height
            if heights[L]<heights[R]:
                L+=1
            # else heigths[L]>heights[R]:
            else:
                R-=1
        
        return result