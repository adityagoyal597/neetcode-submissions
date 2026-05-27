class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for i,operation in enumerate(operations):
            if operation == '+':
                record.append(record[-1]+record[-2])
            elif operation == 'C':
                record.pop()
            elif operation == 'D':
                record.append(2*record[-1])
            else: # Number
                num=int(operation)
                record.append(num)
        
        return sum(record)

        