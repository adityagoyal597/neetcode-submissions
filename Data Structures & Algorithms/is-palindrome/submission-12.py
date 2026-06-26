class Solution:
    def isPalindrome(self, s: str) -> bool:
        L,R=0,len(s)-1

        while L<R:
            #if not (ord('A')<=ord(s[L])<=ord('Z') or ord('a')<=ord(s[L])<=ord('z') or ord('0')<=ord(s[L])<=ord('9')):
            while L<R and not s[L].isalnum():
                L+=1
            #if not (ord('A')<=ord(s[R])<=ord('Z') or ord('a')<=ord(s[R])<=ord('z') or ord('0')<=ord(s[R])<=ord('9')):
            while L<R and not s[R].isalnum():    
                R-=1
            if s[L].lower()!=s[R].lower():
                return False
            # else s[L].lower()==s[R].lower():
            L+=1
            R-=1
        
        return True