class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap={}
        for i in range(numCourses):
            prevMap[i]=[]
        
        for course , preReq in prerequisites:
            prevMap[course].append(preReq)
        
        visit=set()

        def dfs(course):
            if course in visit:
                # detected cycle
                return False
            if prevMap[course]==[]:
                # course has no preRequisites
                return True
            
            visit.add(course)

            for pre in prevMap[course]:
                if not dfs(pre):
                    return False
            
            visit.remove(course)
            prevMap[course]=[]
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
