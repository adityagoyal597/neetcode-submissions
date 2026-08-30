class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj={}

        for airport in range(n):
            adj[airport]=[]
        
        for u,v,cost in flights:
            adj[u].append((cost,v))
        
        cheapestCost={}

        for airport in range(n):
            cheapestCost[airport]={}
        # {airport:{flightTaken:cost}}
        cheapestCost[src][0]=0

        minHeap=[(0,src,0)] #(cost,airport,flightTaken)

        while minHeap:
            cost,node,flightsTaken=heapq.heappop(minHeap)

            if node==dst:
                return cost
            if flightsTaken==k+1: #k stops -> k+1 flights
                continue # can't take more flights
            
            for weight,nextNode in adj[node]:
                newCost=cost+weight
                newFlightsTaken=flightsTaken+1

                if(newFlightsTaken not in cheapestCost[nextNode] or newCost<cheapestCost[nextNode][newFlightsTaken]):
                    cheapestCost[nextNode][newFlightsTaken]=newCost

                    heapq.heappush(minHeap,(newCost,nextNode,newFlightsTaken))
        return -1

