class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)

        adj={}

        for i in range(n):
            adj[i]=[]

        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]

                dist=abs(x1-x2)+abs(y1-y2)

                adj[i].append((dist,j))
                adj[j].append((dist,i))   
        
        visit=set()

        minHeap=[(0,0)]

        totalCost=0

        while len(visit)<n:

            cost,node=heapq.heappop(minHeap)

            if node in visit:
                continue
            
            visit.add(node)

            totalCost+=cost

            for nextCost, nextNode in adj[node]:

                if nextNode not in visit:
                    heapq.heappush(minHeap,(nextCost,nextNode))
        
        return totalCost
