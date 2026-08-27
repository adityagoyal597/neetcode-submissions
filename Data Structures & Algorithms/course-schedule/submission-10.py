class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={}

        for i in range(numCourses):
            adj[i]=[]

        for course,pre in prerequisites:
            adj[course].append(pre)
        
        cycle=set()
        
        def dfs(course):
            if course in cycle:
                return False
            if adj[course]==[]:
                return True
            
            cycle.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            adj[course]=[]
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            
