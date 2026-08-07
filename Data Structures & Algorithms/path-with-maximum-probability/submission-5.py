class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj={}

        for i in range(n):
            adj[i]=[]
        
        for i in range(len(edges)):
            u,v=edges[i]
            p=succProb[i]

            adj[u].append((v,p))
            adj[v].append((u,p))
        
        maxHeap=[(-1,start_node)]

        best={}

        while maxHeap:
            prob,node=heapq.heappop(maxHeap)

            prob=-prob

            if node in best:
                continue
            
            best[node]=prob

            if node ==end_node:
                return prob
            
            for node2,prob2 in adj[node]:
                if node2 not in best:
                    heapq.heappush(maxHeap,(-(prob*prob2),node2))
        return 0