class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={}

        for i in range(numCourses):
            adj[i]=[]
        for course,preReq in prerequisites:
            adj[course].append(preReq)
        
        output=[]
        visit,cycle=set(),set()

        def dfs(course):
            if course in cycle: #visiting twice
                return False
            if course in visit: # already visited
                return True
            
            cycle.add(course)

            for preReq in adj[course]:
                if not dfs(preReq):
                    return False

            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output