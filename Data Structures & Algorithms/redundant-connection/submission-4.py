class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # n nodes -> 1 to n (n-1 edges no cyle)
        # if multiple answers, return edge that appears last

        n=len(edges)
        indegree=[0]*(n+1) # no. of edges connected to each node

        adj={}

        for i in range(n+1):
            adj[i]=[]

        for u,v in edges:
            #undirected graph
            adj[u].append(v)
            adj[v].append(u)

            indegree[u]+=1
            indegree[v]+=1

        queue=deque()

        for i in range(1,n+1):
            # finding all the leaf nodes(indegree==1)
            if indegree[i]==1:
                queue.append(i)
        
        # Keep removing leaves until there are no leaves left.
        while queue:
            node=queue.popleft()
            # revoming it from the graph
            indegree[node]-=1
            # decrementing the indegree of its neighbors as well
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                # if it becomes leaf node then add it to queue
                if indegree[neighbor]==1:
                    queue.append(neighbor)
        
        # nodes remaining after removing the leaf node belong to the cycle
        
        # returns edge that appears last in edges
        for u,v in reversed(edges):
            # node u is part of the cycle and node v is also a part of the cycle
            if indegree[u]==2 and indegree[v]:
                return [u,v]
        return []
        



