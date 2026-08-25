class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L,R=1,max(piles)
        result=R

        while L<=R:
            mid=(L+R)//2

            totalTime=0
            for pile in piles:
                totalTime+=math.ceil(pile/mid)
            
            if totalTime<=h:
                result=mid
                R=mid-1
            else:
                L=mid+1
        
        return result