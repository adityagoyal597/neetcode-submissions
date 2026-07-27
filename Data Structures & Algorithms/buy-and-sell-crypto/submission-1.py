class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #L=Buy,R=Sell
        L=0
        R=0 
        maxProfit=0

        while R<len(prices):

            if prices[L]<prices[R]:
                profit=prices[R]-prices[L]
                maxProfit=max(maxProfit,profit)
            else:
                L=R # found new minimum price to buy 
            R+=1
        return maxProfit