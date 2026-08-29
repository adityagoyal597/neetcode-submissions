class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={}

        for i in range(n):
            adj[i]=[]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit=set()
        components=0

        def bfs(node):
            queue=deque()

            queue.append(node)
            visit.add(node)

            while queue:
                
                node=queue.popleft()
                
                for neighbor in adj[node]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append(neighbor)
        

        for node in range(n):
            if node not in visit:
                bfs(node)
                components+=1
        
        return components

