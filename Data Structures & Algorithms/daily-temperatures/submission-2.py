class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[] #[[index,temp]]

        for index,temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]: 
                colderTempIndex,colderTemp=stack.pop() # listunpacking
                result[colderTempIndex]=index-colderTempIndex
            stack.append([index,temp])
        return result
        