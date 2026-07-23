class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}

        for char in s:
            s_dict[char]=1+s_dict.get(char,0)
        for char in t:
            t_dict[char]=1+t_dict.get(char,0)
        
        return s_dict==t_dict