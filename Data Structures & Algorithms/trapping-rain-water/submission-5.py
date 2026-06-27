class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        L=0
        R=len(height)-1
        leftMax=height[L]
        rightMax=height[R]
        area=0
        while L<R:
            # shift the pointer whose max is min

            if leftMax<=rightMax:
                L+=1
                leftMax=max(leftMax,height[L])
                area+= leftMax -height[L]
            else:
                R-=1
                rightMax=max(rightMax,height[R])
                area+=rightMax-height[R]
        
        return area