class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[] #[[temp,index]]

        for index,temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]: 
                colderTemp,colderTempIndex=stack.pop() # listunpacking
                result[colderTempIndex]=index-colderTempIndex
            stack.append([temp,index])
        return result
        