class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache={} #(i1,i2)->LCS answer dtarting from i1,i2

        def memo(s1,s2,i1,i2,cache):
            if i1==len(s1) or i2==len(s2):
                # longest common subsequence if any of the string is "" is 0
                return 0
            if (i1,i2) in cache:
                return cache[(i1,i2)]
            # characters matched

            if s1[i1]==s2[i2]:
                # adding 1 as s1[i1]==s2[i2]
                cache[(i1,i2)]=1+memo(s1,s2,i1+1,i2+1,cache)
            
            # characters not matched
            else:
                cache[(i1,i2)]=max(
                    memo(s1,s2,i1+1,i2,cache),
                    memo(s1,s2,i1,i2+1,cache)
                )
            return cache[(i1,i2)]

        return memo(text1,text2,0,0,cache)