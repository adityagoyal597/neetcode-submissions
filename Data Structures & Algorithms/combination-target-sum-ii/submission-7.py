class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        curComb=[]

        candidates.sort()

        def dfs(i,total):
            if total==target:
                res.append(curComb.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            curComb.append(candidates[i])

            dfs(i+1,total+candidates[i])

            curComb.pop()

            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            
            dfs(i+1,total)
        
        dfs(0,0)
        return res