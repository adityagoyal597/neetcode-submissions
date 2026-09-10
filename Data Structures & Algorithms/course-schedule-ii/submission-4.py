class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={}

        for i in range(numCourses):
            adj[i]=[]
        
        for course,preReq in prerequisites:
            adj[course].append(preReq)
        
        output=[]
        cycle=set()
        visited=set()

        def dfs(course):

            if course in cycle:
                return False
            
            if course in visited:
                return True

            cycle.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output
