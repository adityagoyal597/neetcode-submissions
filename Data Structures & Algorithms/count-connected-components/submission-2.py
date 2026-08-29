class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components=0
        adj={}        
        visit=set()
        for i in range(n):
            adj[i]=[]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            queue=deque()

            queue.append(node)
            visit.add(node)

            while queue:
                node=queue.popleft()

                for neighbor in adj[node]:
                    if neighbor not in visit:
                        queue.append(neighbor)
                        visit.add(neighbor)

        for i in range(n):
            if i not in visit:
                bfs(i)
                components+=1
        return components
         