class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        letters={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        # result is a list of string
        result=[]

        #curComb to be appended in the result is a string not array
        curComb=""

        def helper(i,digits,curComb,result):

            if i == len(digits):
                result.append(curComb)
                return 
            
            for letter in letters[digits[i]]:
                helper(i+1,digits,curComb+letter,result)
            
        helper(0,digits,curComb,result)
        return result

            

            
             
