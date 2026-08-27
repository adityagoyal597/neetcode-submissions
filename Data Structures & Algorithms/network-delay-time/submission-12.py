class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={}

        for i in range(1, n+1):
            adj[i]=[]

        for src,dst,wei in times:
            adj[src].append((wei,dst))

        shortest={}

        minHeap=[]
        minHeap.append((0,k))

        while minHeap:
            weight1,n1=heapq.heappop(minHeap)

            if n1 in shortest:
                continue

            shortest[n1]=weight1

            for weight2,n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap,(weight1+weight2,n2))
        
        if len(shortest)!=n:
            return -1
        else:
            return max(shortest.values())