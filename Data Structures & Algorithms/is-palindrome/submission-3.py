class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        n=len(s)-1

        while i<n:
            while i<n and not self.alphaNum(s[i]):
                i+=1
            while i<n and not self.alphaNum(s[n]):
                n-=1
            if s[i].lower()!=s[n].lower():
                return False
            i+=1
            n-=1
        return True
    def alphaNum(self,c):
        return (ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9') or ord('A')<=ord(c)<=ord('Z'))