class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree-> no cycle + fully connected
        # connected undirected graph witj n-1 edges can't contain cycle

        # tree with n nodes must have exactly n-1 edges

        if len(edges) != n-1:
            return False
        
        adj={}

        for i in range(n):
            adj[i]=[]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit=set()
        queue=deque()
        queue.append(0)
        visit.add(0)

        while queue:
            node=queue.popleft()

            for neighbor in adj[node]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)

        # every node must be reachable from node 0
        return len(visit)==n