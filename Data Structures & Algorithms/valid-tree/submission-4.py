class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        queue=deque()
        visit=set()
        adj={}

        for i in range(n):
            adj[i]=[]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        queue.append(0)
        visit.add(0)

        while queue:
            node=queue.popleft()

            for neighbor in adj[node]:
                if neighbor not in visit:
                    queue.append(neighbor)
                    visit.add(neighbor)
            
        return len(visit)==n
