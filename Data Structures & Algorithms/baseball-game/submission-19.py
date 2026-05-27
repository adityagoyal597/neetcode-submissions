class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for operation in operations:
            if operation == '+':
                record.append(record[-1]+record[-2])
            elif operation == 'C':
                record.pop()
            elif operation == 'D':
                record.append(2*record[-1])
            else: # Number
                record.append(int(operation))
        
        return sum(record)

        # sum=0
        # for rec in record:
        #     sum+=rec

        # return sum
        