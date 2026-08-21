class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # (i,j)-> min operations
        cache={}
        # minimum number of operations needed to convert word1[i:] into word2[j:]
        def dfs(i,j):

            # insert remaining chars in word2
            if i==len(word1):
                return len(word2)-j
            
            # delete remainanig chars in word1
            if j==len(word2):
                return len(word1)-i
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            # char equal increment both pointers
            if word1[i]==word2[j]:
                cache[(i,j)] = dfs(i+1,j+1)

            # charater not equal , then we have three operation options
            else:
                # insert-> inserted the desired char at previous i , now move to next char in j 
                insert=dfs(i,j+1)
                
                delete=dfs(i+1,j)
                replace=dfs(i+1,j+1)

                cache[(i,j)]=1+min(
                    insert,
                    delete,
                    replace
                )

            return cache[(i,j)]
        
        return dfs(0,0)
