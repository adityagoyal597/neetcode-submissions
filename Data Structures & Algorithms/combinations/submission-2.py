class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb=[]
        curComb=[]

        def helper(i,n,curComb,comb):
            # size of the combination equal to k
            if len(curComb)==k:
                comb.append(curComb.copy())
                return
            # case when all the i's aren't included
            # returns when it exceeds n
            if i>n:
                return 

            # decision when i is included
            curComb.append(i)
            helper(i+1,n,curComb,comb)
            curComb.pop()

            # decision when i isn't included
            helper(i+1,n,curComb,comb)

        
        # combinations from 1 till n 
        helper(1,n,curComb,comb)
        return comb